# Trendshift Report — 2026-04-16
**Total:** 25 repos

---

## 1. [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
> A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**Language:** N/A  |  **Stars:** 54,695  |  **Forks:** 4,633  |  **Score:** 68,175  |  **Created:** 2026-01-27

**Background:** Andrej Karpathy Skills distills Karpathy's widely-discussed observations about LLM coding failure modes into a single CLAUDE.md file. Now at nearly 55,000 stars and climbing rapidly — it jumped from 13,000 four days ago — it has become the de facto reference for configuring Claude Code to avoid known pitfalls.

**Problem it solves:** LLMs make wrong assumptions without verification, overcomplicate APIs and abstractions, produce bloated code where concise solutions exist, and silently remove comments or logic they do not understand. These failure modes compound across sessions and gradually degrade codebase quality in ways that are hard to detect.

**Why another one?** The project repackages authoritative observations from one of the most respected voices in AI into a single drop-in file. Unlike general-purpose guidelines, these rules target specific documented failure modes with concrete countermeasures, and the single-file format makes adoption trivial — no framework, no learning curve.

---

## 2. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
> A collection of DESIGN.md files inspired by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

**Language:** N/A  |  **Stars:** 58,491  |  **Forks:** 7,288  |  **Score:** 12,418  |  **Created:** 2026-03-31

**Background:** Awesome DESIGN.md by VoltAgent curates a collection of DESIGN.md files that capture the design language of popular brands. Now at over 58,000 stars in just over two weeks, it has solidified its place as a go-to resource for developers who want AI agents to produce UI matching real-world design systems.

**Problem it solves:** AI coding agents produce generic, inconsistent UI because they lack visual design context. Describing designs in prose is loose and ambiguous, while Figma exports are unreadable to agents. DESIGN.md files give agents structured design specifications in the format LLMs parse best — markdown with clear sections for colors, typography, spacing, and components.

**Why another one?** The project ships ready-to-use design system files extracted from real brand sites rather than requiring developers to write their own. Dropping one into a project instantly gives any AI coding agent access to a complete, consistent design language — bridging the gap between how agents build and how interfaces should look.

---

## 3. [public-apis](https://github.com/public-apis/public-apis)
> A collective list of free APIs

**Language:** Python  |  **Stars:** 424,774  |  **Forks:** 46,269  |  **Score:** 12,270  |  **Created:** 2016-03-20

**Background:** Public APIs is one of the most popular curated lists on GitHub, with over 424,000 stars accumulated since 2016. It catalogs free, public APIs across dozens of categories — weather, finance, geocoding, music, movies — serving as the default reference for developers hunting for data sources and integrations.

**Problem it solves:** Finding the right public API requires searching across scattered directories, outdated blog posts, and forum threads. API documentation, authentication requirements, and CORS support vary wildly, and discovering whether an API is free, metered, or deprecated often involves trial and error.

**Why another one?** The list benefits from nearly a decade of community curation, with thousands of contributors keeping entries current. Its categorical organization and metadata (auth type, HTTPS, CORS) let developers filter for APIs that match their exact requirements, and the Python tooling around it supports automated validation of entries.

---

## 4. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 159,794  |  **Forks:** 13,929  |  **Score:** 8,867  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a comprehensive skills framework and software development methodology for coding agents, now at nearly 160,000 stars. It enforces a disciplined process — spec extraction, chunked design review, implementation planning, and supervised subagent execution — that keeps agents from jumping straight into code.

**Problem it solves:** AI coding agents default to enthusiasm-without-judgment, writing code before requirements are clear and producing solutions that miss the mark or require extensive rework. Without structured workflows, agents cannot reliably handle multi-step engineering tasks in production contexts.

**Why another one?** Superpowers' subagent-driven development is its key differentiator: it launches specialized sub-agents for each task, inspects their work, and continues autonomously. Skills trigger automatically based on context, and support spans Claude Code, Cursor, Codex, and OpenCode — making it the most broadly compatible skills framework available.

---

## 5. [PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR)
> Open-source, low-cost 10.5 GHz PLFM phased array RADAR system

**Language:** PLSQL  |  **Stars:** 13,824  |  **Forks:** 2,914  |  **Score:** 8,601  |  **Created:** 2026-03-08

**Background:** PLFM_RADAR is an open-source, low-cost 10.5 GHz phased array radar system using pulse linear frequency modulation. With nearly 14,000 stars in just over a month, it has become a rallying point for hardware-hacking enthusiasts and researchers interested in accessible radar technology.

**Problem it solves:** Commercial phased array radar systems are expensive and closed, blocking researchers, students, and independent engineers from studying or modifying their behavior. Academic radar projects typically require specialized lab equipment that is out of reach for most hobbyists.

**Why another one?** The project targets the 10.5 GHz band with an explicit low-cost, open-source design, making phased array radar approachable outside of institutional labs. The release of schematics, firmware, and documentation together gives builders a complete reference implementation rather than fragmented guidance.

---

## 6. [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.

**Language:** Shell  |  **Stars:** 11,792  |  **Forks:** 1,717  |  **Score:** 6,954  |  **Created:** 2026-02-12

**Background:** Claude Code Game Studios transforms Claude Code into a simulated game development studio with 49 AI agents, 72 workflow skills, and a coordination system modeled after real studio hierarchies. With nearly 12,000 stars, it represents an ambitious application of multi-agent orchestration to a creative domain.

**Problem it solves:** Solo developers and small teams cannot replicate the specialized roles of a real game studio — designers, programmers, artists, producers, QA. AI agents can play these roles individually, but without coordination they produce disjointed output that lacks the cohesion of an actual studio.

**Why another one?** The project maps out a complete studio hierarchy rather than offering a flat bag of agents, giving each role clear responsibilities and interaction patterns. The 72 workflow skills cover the end-to-end game dev lifecycle, and the coordination system addresses the hardest problem in multi-agent systems: making them act as a team rather than a committee.

---

## 7. [dive-into-llms](https://github.com/Lordog/dive-into-llms)
> 《动手学大模型Dive into LLMs》系列编程实践教程

**Language:** Jupyter Notebook  |  **Stars:** 32,425  |  **Forks:** 3,935  |  **Score:** 5,330  |  **Created:** 2024-04-08

**Background:** Dive into LLMs is a Chinese-language hands-on tutorial series for large language models, now at over 32,000 stars. Styled after the influential Dive into Deep Learning textbook, it covers LLM programming practice through Jupyter notebooks that walk through training, fine-tuning, and deployment.

**Problem it solves:** Chinese-speaking developers and students often face a gap between theoretical LLM resources and practical, executable tutorials in their native language. Existing English-language materials require translation friction, and many lack the hands-on code that makes concepts stick.

**Why another one?** The tutorial's notebook-first format ensures every concept has runnable code, and the Chinese-language delivery serves a large audience underserved by English resources. Its comprehensive coverage — from basics through advanced topics — makes it usable both as a classroom text and a self-study guide.

---

## 8. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 97,902  |  **Forks:** 13,800  |  **Score:** 5,234  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is a self-improving AI agent approaching 100,000 stars. It features a built-in learning loop that creates skills from experience and builds a deepening model of the user across sessions, making it the most widely-starred agent with true cross-session learning.

**Problem it solves:** Most AI agents start from zero in every session — no memory of past interactions, no learning from mistakes, no adaptation to user preferences. Users re-explain context repeatedly, and the agent never develops the domain expertise that makes human assistants valuable.

**Why another one?** Hermes Agent's learning loop is its core differentiator: skills created from experience improve during use, and persistent user models carry across sessions. It runs on infrastructure from a $5 VPS to a GPU cluster, supports 200+ models via OpenRouter, and operates across Telegram, Discord, Slack, WhatsApp, and Signal from a single gateway.

---

## 9. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> from vibe coding to agentic engineering - practice makes claude perfect

**Language:** HTML  |  **Stars:** 45,972  |  **Forks:** 4,468  |  **Score:** 4,663  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice is a continuously updated guide for moving from unstructured "vibe coding" to disciplined agentic engineering with Claude Code. Now at nearly 46,000 stars and up roughly 9,000 from four days ago, it provides best practices, implementation guides, and orchestration workflows tied to the latest Claude Code releases.

**Problem it solves:** Developers using Claude Code often default to unstructured prompting, producing inconsistent results. Without systematic practices for specification, orchestration, and quality control, the AI agent becomes a fast but undisciplined coder — and the undiscipline compounds across a codebase over time.

**Why another one?** The project is continuously updated to match the latest Claude Code releases, with version-tagged badges showing currency. Its progression from best practices to implementation to orchestration gives developers a learning path rather than just a reference document, and the HTML-first format makes it easy to browse.

---

## 10. [claude-mem](https://github.com/thedotmack/claude-mem)
> A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**Language:** TypeScript  |  **Stars:** 63,104  |  **Forks:** 5,284  |  **Score:** 4,178  |  **Created:** 2025-08-31

**Background:** Claude-mem is a Claude Code plugin that captures everything from coding sessions, compresses it with the Claude Agent SDK, and injects relevant context into future sessions. Now at over 63,000 stars, it tackles the central limitation of stateless coding agents through AI-assisted summarization.

**Problem it solves:** Claude Code sessions lose all context when they end — decisions made, debugging insights discovered, architecture discussions resolved. Developers either re-explain everything in the next session or paste long context blocks manually, and critical nuance gets lost either way.

**Why another one?** Claude-mem uses Claude's own agent-sdk to compress session history rather than relying on keyword extraction or simple summarization, preserving reasoning and intent. The automatic capture-and-inject loop requires zero manual curation, and the plugin architecture means it layers on top of existing Claude Code workflows without disrupting them.

---

## 11. [caveman](https://github.com/JuliusBrussee/caveman)
> 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**Language:** Python  |  **Stars:** 37,069  |  **Forks:** 1,789  |  **Score:** 3,975  |  **Created:** 2026-04-04

**Background:** Caveman is a Claude Code skill that slashes token consumption by rewriting agent output in compressed caveman-style language. Created less than two weeks ago, it has surged past 37,000 stars, reflecting strong demand for token-cost optimization in AI coding workflows.

**Problem it solves:** AI coding agents are verbose by default — polite phrasing, redundant explanations, and stylistic flourishes consume tokens that add no functional value. This drives up API costs and slows down interactions, especially in long sessions with extensive back-and-forth between user and agent.

**Why another one?** Caveman's approach is uniquely playful yet effective: rather than complex prompt engineering or output filtering, it teaches the agent to communicate in compressed language. The claimed 65% token reduction translates directly into cost savings, and installation is a single command into any Claude Code setup.

---

## 12. [GenericAgent](https://github.com/lsdefine/GenericAgent)
> Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption

**Language:** Python  |  **Stars:** 4,506  |  **Forks:** 481  |  **Score:** 3,528  |  **Created:** 2026-01-16

**Background:** GenericAgent is a self-evolving agent that grows a skill tree from a compact 3,300-line seed, reaching full system control with 6x less token consumption than comparable frameworks. With over 4,500 stars, it represents a minimalist take on agent architecture that emphasizes bootstrapping over configuration.

**Problem it solves:** Most agent frameworks ship with thousands of lines of preset logic, tools, and skills that consume context and often do not match what users actually need. Scaling agent capabilities typically means expanding the framework itself rather than letting the agent grow its own skill set.

**Why another one?** The 3.3K-line seed and 6x token reduction claim differentiate GenericAgent from bloated frameworks. Self-evolution — growing skills from experience rather than from prewritten playbooks — creates agents tailored to the specific tasks users run, and the minimal codebase makes the framework itself auditable.

---

## 13. [open-lovable](https://github.com/firecrawl/open-lovable)
> 🔥 Clone and recreate any website as a modern React app in seconds

**Language:** TypeScript  |  **Stars:** 25,688  |  **Forks:** 4,928  |  **Score:** 3,472  |  **Created:** 2025-08-08

**Background:** Open Lovable by Firecrawl clones and recreates any website as a modern React app in seconds. With over 25,000 stars, it combines Firecrawl's web scraping expertise with LLM-driven code generation to convert arbitrary web pages into maintainable React codebases.

**Problem it solves:** Rebuilding an existing website in a modern framework is tedious — developers must inspect DOM, extract styles, reconstruct layout, and translate interactions by hand. Traditional website-to-code tools produce unmaintainable HTML/CSS dumps rather than idiomatic React components.

**Why another one?** Open Lovable's pipeline is purpose-built for React output rather than raw HTML, producing code developers would actually ship. The Firecrawl integration handles the messy web-extraction side reliably, and the open-source model offers a self-hosted alternative to commercial website-to-React services.

---

## 14. [editor](https://github.com/pascalorg/editor)
> Create and share 3D architectural projects.

**Language:** TypeScript  |  **Stars:** 13,251  |  **Forks:** 1,612  |  **Score:** 3,434  |  **Created:** 2025-10-16

**Background:** Pascal Editor is an open-source 3D editor for architectural projects with over 13,000 stars. It provides a browser-based tool for creating, editing, and sharing 3D building designs, positioned as an accessible alternative to desktop architectural software.

**Problem it solves:** Professional architectural tools like Revit and SketchUp are expensive and have steep learning curves, locking out students, hobbyists, and small firms. Browser-based alternatives historically sacrificed capability for accessibility, leaving a gap for serious but approachable 3D architecture tools.

**Why another one?** Pascal Editor lives entirely in the browser with sharing baked in, making collaboration and publication trivial. The TypeScript implementation gives developers a hackable foundation, and the open-source license means architectural firms can self-host and extend it for team-specific workflows.

---

## 15. [Decepticon](https://github.com/PurpleAILAB/Decepticon)
> Autonomous Hacking Agent for Red Team Testing

**Language:** Python  |  **Stars:** 2,264  |  **Forks:** 391  |  **Score:** 3,384  |  **Created:** 2025-06-06

**Background:** Decepticon is an autonomous hacking agent designed for red team testing, developed by PurpleAILAB. With over 2,200 stars, it brings AI-driven autonomy to offensive security testing — a domain traditionally reliant on human expertise and manual tooling.

**Problem it solves:** Red team exercises are expensive, slow, and constrained by the availability of skilled testers. Manual penetration testing cannot match the scale of modern attack surfaces, and existing automated tools are largely signature-based rather than adaptive.

**Why another one?** Decepticon applies agent-based autonomy — reasoning, tool use, planning — to offensive security in a way that static scanners cannot. Its red-team framing sets a clear, defensive intent, and the open-source model lets security teams audit the agent's behavior rather than trusting a black-box commercial product.

---

## 16. [voicebox](https://github.com/jamiepine/voicebox)
> The open-source voice synthesis studio

**Language:** TypeScript  |  **Stars:** 19,836  |  **Forks:** 2,278  |  **Score:** 3,379  |  **Created:** 2026-01-25

**Background:** Voicebox by Jamie Pine is an open-source voice synthesis studio at nearly 20,000 stars. It provides a complete environment for voice generation, editing, and cloning, positioned as the open alternative to commercial services like ElevenLabs and PlayHT.

**Problem it solves:** Commercial voice synthesis services lock users into subscription tiers, API rate limits, and proprietary voice libraries. Creators building podcasts, videos, and games need studio-grade voice control without sending every line through a third-party server.

**Why another one?** Voicebox's studio framing — not just an API but a full editing environment — differentiates it from SDK-only open-source TTS projects. The TypeScript stack makes it approachable for web developers, and the open-source license enables self-hosting for teams with privacy or cost constraints.

---

## 17. [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
> An AI Hedge Fund Team

**Language:** Python  |  **Stars:** 56,277  |  **Forks:** 9,771  |  **Score:** 3,177  |  **Created:** 2024-11-29

**Background:** AI Hedge Fund is a proof-of-concept AI-powered investment team with over 56,000 stars. It deploys multiple agents modeled after famous investors — Damodaran, Graham, Ackman, Wood, Munger — each applying their distinct investment philosophies to analyze stocks and make trading recommendations.

**Problem it solves:** Investment analysis requires synthesizing multiple frameworks — value, growth, activist, quantitative — that individual analysts rarely master simultaneously. Getting diverse perspectives on a stock traditionally requires a full team of specialists, which is out of reach for individual investors and small firms.

**Why another one?** The multi-agent persona approach makes the reasoning process transparent and educational — users see how a Graham-style value analysis differs from a Cathie Wood growth thesis on the same stock. The explicit educational framing sets clear expectations that the project is a learning tool rather than production trading software.

---

## 18. [tegaki](https://github.com/KurtGokhan/tegaki)
> Handwriting animation for the web. Supports any font or text.

**Language:** TypeScript  |  **Stars:** 1,868  |  **Forks:** 56  |  **Score:** 3,140  |  **Created:** 2026-03-28

**Background:** Tegaki is a handwriting animation library for the web that supports any font or text input. Created about three weeks ago and now at nearly 1,900 stars, it brings the visual charm of stroke-by-stroke handwriting reveal to any website with minimal setup.

**Problem it solves:** Creating handwriting-style animations on the web typically requires custom SVG authoring, frame-by-frame CSS animation, or heavy motion graphics tools. Developers who want a simple "text appears as if written by hand" effect face an outsized implementation burden.

**Why another one?** Tegaki's universal font support — any font, any text — is the killer feature: designers are not locked into a prebaked handwriting style. The lightweight TypeScript implementation integrates cleanly into any modern web stack, and the declarative API makes common cases a few lines of code.

---

## 19. [skills](https://github.com/anthropics/skills)
> Public repository for Agent Skills

**Language:** Python  |  **Stars:** 120,404  |  **Forks:** 13,955  |  **Score:** 2,954  |  **Created:** 2025-09-22

**Background:** Anthropic's official Skills repository provides the canonical public collection of Agent Skills for Claude. With over 120,000 stars, it serves as the reference implementation that third-party skills build against, and the source of truth for the skill format specification.

**Problem it solves:** Without an authoritative reference, third-party skill authors face inconsistent conventions, unclear format specifications, and no centralized discovery mechanism. Users hunting for high-quality, well-maintained skills have to sift through variable-quality community repositories.

**Why another one?** As the official repository from Anthropic, it guarantees format currency, security review, and long-term maintenance. Skills published here set the baseline for quality and serve as templates for community skill authors, and centralized discoverability reduces the friction of finding production-ready skills.

---

## 20. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 115,798  |  **Forks:** 19,303  |  **Score:** 2,712  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official agentic coding tool that lives in the terminal, now at nearly 116,000 stars. It understands codebases, executes routine tasks, explains complex code, and manages git workflows — all driven by natural language — and has become the reference agent for terminal-first AI coding workflows.

**Problem it solves:** Developers who live in the terminal are underserved by browser-based AI coding tools — context switching breaks flow, and most tools do not integrate cleanly with git, shells, or local file operations. Claude Code brings agentic capabilities directly into the terminal environment where power users already work.

**Why another one?** As the first-party Anthropic tool, Claude Code has direct access to the latest Claude capabilities and the most idiomatic agent patterns. Its terminal-native design preserves developer flow, the skills ecosystem built around it extends its capabilities without bloat, and the git-aware workflows address real-world engineering tasks rather than toy demos.

---

## 21. [hello-agents](https://github.com/datawhalechina/hello-agents)
> 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**Language:** Python  |  **Stars:** 38,479  |  **Forks:** 4,567  |  **Score:** 2,698  |  **Created:** 2025-09-07

**Background:** Hello Agents by Datawhale is a Chinese-language textbook titled "Building Agents from Scratch" that covers agent principles and practical tutorials. Now at over 38,000 stars, it is among the most popular Chinese-language resources for learning AI agent development.

**Problem it solves:** Chinese-speaking developers and students lack comprehensive, in-language resources that cover agent architecture from first principles through working implementations. English-language materials exist but introduce translation friction, and most Chinese tutorials focus on narrow tooling rather than underlying theory.

**Why another one?** The project pairs theoretical grounding with hands-on implementation exercises, giving readers both the why and the how. Its Datawhale backing — a respected Chinese AI education community — ensures continuity and quality, and the textbook format makes it usable as classroom material or self-study.

---

## 22. [Apollo-11](https://github.com/chrislgarry/Apollo-11)
> Original Apollo 11 Guidance Computer (AGC) source code for the command and lunar modules.

**Language:** Assembly  |  **Stars:** 67,331  |  **Forks:** 7,652  |  **Score:** 2,667  |  **Created:** 2014-04-03

**Background:** Apollo-11 hosts the original Apollo 11 Guidance Computer source code for the command and lunar modules, transcribed from NASA archives. With over 67,000 stars accumulated over a decade, it is a cultural touchstone of the open-source movement and a favorite topic of space and computing history discussions.

**Problem it solves:** Historical source code from landmark computing projects is often buried in government archives, paper printouts, or institutional repositories inaccessible to the public. Without version-controlled, browsable access, this code cannot be studied, annotated, or preserved by the broader engineering community.

**Why another one?** The project provides the complete command module and lunar module source in a single, searchable GitHub repository with community-contributed comments and annotations. Its educational and historical value is unmatched — few projects let engineers read the exact code that took humans to the Moon.

---

## 23. [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)
> Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

**Language:** Python  |  **Stars:** 3,677  |  **Forks:** 321  |  **Score:** 2,505  |  **Created:** 2026-04-10

**Background:** Fireworks Tech Graph is a Claude Code skill that turns natural language descriptions into polished SVG+PNG technical diagrams. Created just six days ago, it has already amassed over 3,600 stars, with expanding support for diagram types, visual styles, and UML — reflecting the rapid pace of the Claude Code skills ecosystem.

**Problem it solves:** Technical diagrams — architecture charts, flow diagrams, sequence diagrams — typically require specialized tools like Mermaid, Excalidraw, or draw.io. These tools interrupt the coding workflow and require tool-specific syntax that developers rarely keep fresh in memory.

**Why another one?** The skill operates entirely within Claude Code via natural language, eliminating the context switch to external diagramming tools. It generates both SVG (for editing) and PNG (for sharing) in one command, and its deep AI/Agent domain knowledge produces accurate representations of common system architectures out of the box.

---

## 24. [leetcode-patterns](https://github.com/seanprashad/leetcode-patterns)
> A pattern-based approach to learn technical interview questions

**Language:** TypeScript  |  **Stars:** 12,508  |  **Forks:** 2,024  |  **Score:** 2,478  |  **Created:** 2018-12-31

**Background:** LeetCode Patterns is a pattern-based guide for technical interview preparation, now at over 12,000 stars. Rather than listing problems individually, it groups them by underlying algorithmic pattern — sliding window, two pointers, dynamic programming — to help candidates build transferable problem-solving skills.

**Problem it solves:** Memorizing hundreds of individual LeetCode problems is inefficient and fragile — candidates freeze when they see a variant they have not seen before. Pattern-based learning teaches the general strategy that solves entire classes of problems, producing more robust interview performance.

**Why another one?** The site's curated pattern groupings distill collective interview prep wisdom into a structured learning path. The progress tracking UI, company-specific filtering, and difficulty sorting let candidates tailor their prep to target roles, and the open-source model keeps the curation community-driven rather than paywalled.

---

## 25. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞

**Language:** TypeScript  |  **Stars:** 359,472  |  **Forks:** 73,161  |  **Score:** 2,442  |  **Created:** 2025-11-24

**Background:** OpenClaw is a personal AI assistant with over 359,000 stars — one of the most popular open-source projects on GitHub. Supporting any OS and any platform, it delivers a full-featured AI assistant experience with self-hosting capabilities and a distinctive lobster-themed identity.

**Problem it solves:** Commercial AI assistants lock users into specific platforms, limit customization, and raise privacy concerns by routing all data through corporate servers. Developers and power users want an AI assistant they can self-host, customize, and integrate into their own workflows without vendor restrictions.

**Why another one?** OpenClaw's massive community — 359K stars, 73K forks — creates a self-reinforcing ecosystem of plugins, integrations, and shared configurations. The cross-platform support and self-hosted architecture give users full control, and the rapid development pace keeps it current with the latest AI model releases across providers.

---

> **Day's theme:** Today's chart crowns Claude Code configuration and skill packaging as the dominant motif — forrestchang/andrej-karpathy-skills leaps to the top with a 68K score as a single CLAUDE.md, while VoltAgent's DESIGN.md collection, Superpowers, Claude Code Game Studios, Claude-mem, Caveman, Fireworks Tech Graph, and Anthropic's own skills and claude-code repos occupy roughly a third of the chart. Alongside the skills wave, a strong infrastructure and self-hosting strand appears — OpenClaw (359K stars) and Hermes Agent (97K stars) continue their run as self-hosted AI assistant platforms, complemented by domain-specific agents like Decepticon for red team testing and AI Hedge Fund for investment analysis. A quieter undertone of learning resources (dive-into-llms, hello-agents, leetcode-patterns, Apollo-11) and creative tooling (voicebox, tegaki, pascal editor, open-lovable) rounds out a day where the meta-layer — how humans configure agents, and how agents configure each other — continues to eclipse the underlying models themselves.
