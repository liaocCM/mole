# Trendshift Report — 2026-04-07
**Total:** 25 repos

---

## 1. [career-ops](https://github.com/santifer/career-ops)
> AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

**Language:** Go  |  **Stars:** 3,845  |  **Forks:** 585  |  **Score:** 50,719  |  **Created:** 2026-04-04

**Background:** Career-Ops is an AI-powered job search pipeline built on Claude Code that turns the agent into a full job search command center. Created just three days ago, it has already amassed nearly 4,000 stars, reflecting strong demand for AI-assisted career tools. It provides 14 skill modes covering everything from offer evaluation to batch PDF generation.

**Problem it solves:** Job searching involves repetitive, time-consuming tasks: tailoring resumes per listing, evaluating fit across dozens of postings, and tracking application status in spreadsheets. Career-Ops automates this pipeline end-to-end, using AI agents to navigate career portals with Playwright, score offers on 10 weighted dimensions, and generate ATS-optimized CVs customized per job description.

**Why another one?** Unlike spray-and-pray automation tools, Career-Ops is designed as a filter that recommends against applying to low-scoring positions. Its Go dashboard and structured scoring system treat the job search as an engineering problem, and the batch processing capability lets users evaluate 10+ offers in parallel with sub-agents.

---

## 2. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
> Collection of DESIGN.md files that capture design systems from popular websites. Drop one into your project and let coding agents build matching UI.

**Language:** HTML  |  **Stars:** 15,726  |  **Forks:** 1,933  |  **Score:** 48,667  |  **Created:** 2026-03-31

**Background:** Awesome DESIGN.md is a curated collection of DESIGN.md files that capture design systems from popular websites, maintained by VoltAgent. With over 15,000 stars in just a week since launch, it has become one of the fastest-growing repositories in the AI coding space. The project builds on Google Stitch's DESIGN.md concept — a plain-text design system document that AI agents read to generate consistent UI.

**Problem it solves:** AI coding agents produce generic, inconsistent UI because they lack visual design context. Developers either describe designs in prose (which agents interpret loosely) or export Figma files (which agents cannot read). DESIGN.md files give agents structured design specifications in the format LLMs read best — markdown.

**Why another one?** The project provides ready-to-use design system files extracted from real websites rather than requiring developers to write their own. With 58 DESIGN.md files covering popular sites, developers can drop one into their project and get pixel-perfect UI matching a known design system, bridging the gap between AGENTS.md (how to build) and DESIGN.md (how it should look).

---

## 3. [agent-skills](https://github.com/addyosmani/agent-skills)
> Production-grade engineering skills for AI coding agents.

**Language:** Shell  |  **Stars:** 4,207  |  **Forks:** 444  |  **Score:** 11,872  |  **Created:** 2026-02-15

**Background:** Agent Skills by Addy Osmani provides production-grade engineering skills for AI coding agents, packaging the workflows and quality gates that senior engineers use into seven slash commands mapped to the development lifecycle. Originally released in February 2026, it continues to gain traction with over 4,200 stars.

**Problem it solves:** AI coding agents jump straight into writing code without following the disciplined processes that experienced engineers use — specifying requirements, planning incrementally, testing thoroughly, and reviewing before shipping. This leads to code that works in isolation but fails in production contexts.

**Why another one?** The skills activate automatically based on context — designing an API triggers the api-and-interface-design skill, building UI triggers frontend-ui-engineering. This means developers get structured workflows without needing to remember which skill to invoke. The plugin marketplace integration with Claude Code makes installation a single command.

---

## 4. [graphify](https://github.com/safishamsi/graphify)
> AI coding assistant skill (Claude Code, Codex, OpenCode, OpenClaw). Turn any folder of code, docs, papers, or images into a queryable knowledge graph

**Language:** Python  |  **Stars:** 2,334  |  **Forks:** 216  |  **Score:** 7,507  |  **Created:** 2026-04-03

**Background:** Graphify is a Claude Code skill that reads any folder of code, docs, papers, or images and builds a queryable knowledge graph from the content. Created just four days ago, it has already gained over 2,300 stars. It is fully multimodal, using Claude's vision capabilities to extract concepts from screenshots, diagrams, and whiteboard photos alongside traditional text.

**Problem it solves:** Developers and researchers accumulate large collections of heterogeneous files — code, PDFs, markdown notes, screenshots — with no way to see relationships between them. Reading raw files is token-expensive and lacks structural insight. Graphify claims 71.5x fewer tokens per query compared to reading raw files, with persistent graphs that survive across sessions.

**Why another one?** Unlike browser-based tools, Graphify runs as a native Claude Code skill invoked with a single slash command. Its multimodal ingestion handles images in any language, and its output includes an interactive HTML graph, an Obsidian vault, Wikipedia-style articles, and a structured JSON graph that can be queried weeks later without re-processing.

---

## 5. [goose](https://github.com/aaif-goose/goose)
> an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

**Language:** Rust  |  **Stars:** 38,206  |  **Forks:** 3,705  |  **Score:** 5,862  |  **Created:** 2024-08-23

**Background:** Goose is an open-source, general-purpose AI agent that recently moved from Block to the Agentic AI Foundation (AAIF) at the Linux Foundation. With over 38,000 stars, it is one of the most established open-source AI agents, offering a native desktop app for macOS, Linux, and Windows alongside a full CLI and API.

**Problem it solves:** Most AI tools are limited to code suggestions within an IDE, leaving developers to manually handle installation, execution, testing, and debugging. Goose goes beyond suggestions to actually install dependencies, execute commands, edit files, and run tests — acting as a full-fledged agent rather than an autocomplete engine.

**Why another one?** Goose's move to the Linux Foundation signals institutional commitment to open governance. It supports 15+ LLM providers and connects to 70+ extensions via the Model Context Protocol. The Rust implementation provides performance advantages, and users can leverage existing Claude, ChatGPT, or Gemini subscriptions without separate API keys.

---

## 6. [claw-code](https://github.com/ultraworkers/claw-code)
> The repo is finally unlocked. enjoy the party! The fastest repo in history to surpass 100K stars ⭐. Join Discord: https://discord.gg/5TUQKqFWd Built in Rust using oh-my-codex.

**Language:** Rust  |  **Stars:** 173,712  |  **Forks:** 105,051  |  **Score:** 5,694  |  **Created:** 2026-03-31

**Background:** Claw Code is a Rust reimplementation of a CLI agent harness that became the fastest repository in GitHub history to surpass 100,000 stars, now sitting at over 173,000. Built using the oh-my-codex framework, it has attracted massive attention since its March 31 launch and continues to trend strongly.

**Problem it solves:** Existing CLI agent harnesses are primarily written in TypeScript or Python, introducing runtime dependencies and performance overhead for terminal-centric workflows. Claw Code provides a native Rust binary that eliminates these dependencies while maintaining feature parity with established agent harnesses.

**Why another one?** The sheer velocity of community adoption — 173,000 stars in eight days — suggests Claw Code fills a gap for developers wanting a performant, compiled agent harness. The project maintains detailed parity documentation tracking its progress against the reference implementation, and the container-first workflow supports deployment beyond local development.

---

## 7. [RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot)
> Create Reddit Videos with just✨ one command ✨

**Language:** Python  |  **Stars:** 9,316  |  **Forks:** 2,352  |  **Score:** 5,497  |  **Created:** 2022-05-26

**Background:** RedditVideoMakerBot is a Python tool that automates the creation of Reddit-style narrated videos popular on TikTok, YouTube, and Instagram. Originally launched in May 2022, it has accumulated over 9,300 stars and continues to trend, indicating sustained interest in automated short-form content creation.

**Problem it solves:** Reddit narration videos get millions of views across social platforms but require manual effort to produce — selecting posts, generating voiceovers, editing clips, and assembling the final video. This bot automates the entire pipeline with a single command, removing the editing and asset-compilation bottleneck.

**Why another one?** As one of the oldest and most battle-tested tools in this space, RedditVideoMakerBot benefits from years of community contributions and bug fixes. Its single-command execution model and Playwright-based automation make it accessible to non-technical users who want to participate in the Reddit content creation trend.

---

## 8. [feynman](https://github.com/getcompanion-ai/feynman)
> No description provided.

**Language:** TypeScript  |  **Stars:** 2,613  |  **Forks:** 305  |  **Score:** 5,306  |  **Created:** 2026-03-19

**Background:** Feynman is an open-source AI research agent by Companion AI that operates from the terminal. With over 2,600 stars since its March 2026 launch, it provides a focused research workflow combining paper search, web research, and multi-agent deep investigation capabilities.

**Problem it solves:** Research tasks require searching across papers and the web, synthesizing findings, verifying claims, and producing cited briefs — a workflow that existing coding agents handle poorly because they are optimized for code generation rather than research methodology. Feynman provides purpose-built commands for literature reviews, deep research, and cited synthesis.

**Why another one?** Feynman's skills-only installation option lets users add research capabilities to existing Claude Code or Codex setups without replacing their primary agent. The multi-agent deep research mode runs parallel researchers with synthesis and verification, producing more thorough results than single-pass queries.

---

## 9. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 74,280  |  **Forks:** 11,645  |  **Score:** 4,730  |  **Created:** 2025-10-13

**Background:** The Agency is a collection of over 74,000-star AI agent personalities, each a meticulously crafted specialist with unique voice, expertise, and deliverables. Born from a Reddit thread and months of iteration, it provides ready-to-use agent configurations for everything from frontend development to community management.

**Problem it solves:** Generic AI prompts produce generic results. Teams need specialists — a frontend developer who follows React best practices, a DevOps engineer who writes proper Terraform, a community manager who understands Reddit dynamics. The Agency provides these specialists as pre-built, personality-driven agents with battle-tested workflows.

**Why another one?** Each agent includes not just a system prompt but complete identity traits, core missions, technical deliverables with code examples, and success metrics. The agents work with Claude Code, Cursor, and other tools, making them portable across the AI coding ecosystem.

---

## 10. [developer-icons](https://github.com/xandemon/developer-icons)
> A collection of well-optimized SVG tech logos for developers and designers—customizable, scalable, and free.

**Language:** TypeScript  |  **Stars:** 724  |  **Forks:** 70  |  **Score:** 4,670  |  **Created:** 2023-11-20

**Background:** Developer Icons is a collection of well-optimized SVG tech logos available as a React component library and CDN. Originally created in November 2023, it provides scalable, customizable icons for developers and designers building tech-related interfaces.

**Problem it solves:** Developers building portfolio sites, documentation, or tech comparison pages need consistent, high-quality technology logos. Sourcing SVGs from individual brand pages is tedious, and the results vary in quality, sizing, and optimization. Developer Icons provides a single, curated source with consistent formatting.

**Why another one?** The library is available as both an npm package with React components and a CDN for direct use, covering the two most common integration patterns. All icons are optimized SVGs that scale cleanly, and the project maintains an interactive gallery at its documentation site for easy browsing.

---

## 11. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 138,686  |  **Forks:** 11,746  |  **Score:** 4,369  |  **Created:** 2025-10-09

**Background:** Superpowers is an agentic skills framework and software development methodology by Jesse Vincent (obra) that has grown to over 138,000 stars. It provides a complete workflow that starts from spec creation through implementation planning and subagent-driven development, enabling hours of autonomous agent operation.

**Problem it solves:** AI coding agents tend to jump directly into writing code without proper planning, producing solutions that miss requirements or need extensive rework. Superpowers enforces a structured workflow: spec extraction, design review in digestible chunks, implementation planning, and supervised subagent execution.

**Why another one?** Superpowers' subagent-driven development process is its key differentiator — it launches sub-agents for each engineering task, inspects and reviews their work, and continues forward autonomously. The skills trigger automatically based on context, requiring no manual activation, and the framework supports Claude Code, Cursor, Codex, and OpenCode.

---

## 12. [obsidian-skills](https://github.com/kepano/obsidian-skills)
> Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI.

**Language:** N/A  |  **Stars:** 21,319  |  **Forks:** 1,312  |  **Score:** 4,224  |  **Created:** 2026-01-02

**Background:** Obsidian Skills by Kepano (the creator of Obsidian) provides agent skills for working with Obsidian's ecosystem — Markdown, Bases, JSON Canvas, and the CLI. With over 21,000 stars, it is the official guide for AI agents interacting with Obsidian vaults.

**Problem it solves:** AI agents produce generic markdown that ignores Obsidian-specific syntax like wikilinks, embeds, callouts, and properties. They also cannot work with Obsidian Bases or JSON Canvas files without explicit guidance. These skills teach agents the correct syntax and patterns for each Obsidian file type.

**Why another one?** As the official skill set from Obsidian's creator, these skills carry authoritative knowledge of Obsidian's conventions. They follow the Agent Skills specification for cross-platform compatibility with Claude Code, Codex CLI, and OpenCode, and are available via marketplace install for zero-friction setup.

---

## 13. [My-Brain-Is-Full-Crew](https://github.com/gnekt/My-Brain-Is-Full-Crew)
> Built by a PhD whose memory was failing, whose diet was a mess, and whose anxiety had its own agenda. Most second brain tools ignore the fact that your brain doesn't work in isolation: your body and your mental health are part of the system too. This crew handles all three: knowledge, nutrition, and mental wellness.

**Language:** Shell  |  **Stars:** 2,142  |  **Forks:** 218  |  **Score:** 3,914  |  **Created:** 2026-03-21

**Background:** My Brain Is Full Crew is a team of 8+ AI agents and 13 specialized skills that manage an Obsidian vault, created by a PhD researcher whose memory was failing. It goes beyond typical second-brain tools by addressing not just knowledge management but also nutrition tracking and mental wellness.

**Problem it solves:** Existing Obsidian AI integrations are essentially glorified search engines — they help find notes but do not help organize, file, connect, or triage information. For someone overwhelmed by cognitive load, search is not enough; they need a system that proactively organizes incoming information, transcribes conversations, and triages email.

**Why another one?** The crew's holistic approach — managing knowledge, nutrition, and mental health in a single system — reflects its origin as a personal tool built by someone dealing with cognitive overload. The 8+ agents handle distinct responsibilities (filing, connecting, searching, transcribing, email triage) and work in any language.

---

## 14. [shannon](https://github.com/KeygraphHQ/shannon)
> Shannon Lite is an autonomous, white-box AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production.

**Language:** TypeScript  |  **Stars:** 37,028  |  **Forks:** 3,915  |  **Score:** 3,821  |  **Created:** 2025-09-27

**Background:** Shannon by Keygraph is an autonomous, white-box AI pentester for web applications and APIs that has accumulated over 37,000 stars. It analyzes source code, identifies attack vectors, and executes real exploits to prove vulnerabilities with working proof-of-concept demonstrations before they reach production.

**Problem it solves:** Teams using AI coding tools like Claude Code and Cursor ship code continuously, but penetration tests happen once a year at most. This creates a 364-day security gap where vulnerabilities can be unknowingly deployed to production. Shannon provides on-demand, automated penetration testing that can run against every build.

**Why another one?** Shannon's white-box approach — combining source code analysis with live exploitation — produces higher-quality findings than black-box scanners. Only vulnerabilities with working proof-of-concept exploits are included in reports, eliminating false positives. Its TypeScript implementation and npm distribution make it accessible to the web development teams who need it most.

---

## 15. [qmd](https://github.com/tobi/qmd)
> mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local

**Language:** TypeScript  |  **Stars:** 19,409  |  **Forks:** 1,167  |  **Score:** 3,609  |  **Created:** 2025-12-08

**Background:** QMD (Query Markup Documents) by Tobi is a local-first CLI search engine for markdown notes, meeting transcripts, documentation, and knowledge bases. With over 19,000 stars, it combines BM25 full-text search, vector semantic search, and LLM re-ranking — all running locally via node-llama-cpp with GGUF models.

**Problem it solves:** Developers and knowledge workers accumulate markdown files across multiple directories — notes, meeting transcripts, documentation — but have no unified way to search across them. Cloud-based search tools require uploading sensitive content, and basic grep lacks semantic understanding.

**Why another one?** QMD's hybrid search approach (keyword + semantic + LLM re-ranking) provides better results than any single method alone, and everything runs locally with no API keys or cloud dependencies. Its context system lets users annotate collections with metadata that improves search relevance, and the CLI-first design integrates naturally into agentic workflows.

---

## 16. [gallery](https://github.com/google-ai-edge/gallery)
> A gallery that showcases on-device ML/GenAI use cases and allows people to try and use models locally.

**Language:** Kotlin  |  **Stars:** 18,293  |  **Forks:** 1,706  |  **Score:** 3,500  |  **Created:** 2025-03-31

**Background:** Google AI Edge Gallery is an official Google project that showcases on-device ML and GenAI use cases, allowing users to run powerful open-source LLMs directly on mobile devices. Now featuring Gemma 4, it provides a premier destination for experiencing on-device AI on both Android and iOS.

**Problem it solves:** Trying large language models typically requires cloud APIs, subscriptions, and sending data to remote servers. For privacy-sensitive or offline use cases, there is no easy way to experience state-of-the-art AI models. Gallery lets users run models like Gemma 4 entirely on their device — fully offline, private, and without API costs.

**Why another one?** As an official Google project available on both Google Play and the App Store, Gallery carries institutional backing and receives early support for new model releases like Gemma 4. The focus on mobile deployment differentiates it from desktop-oriented local LLM tools, targeting the growing demand for AI capabilities on phones and tablets.

---

## 17. [seomachine](https://github.com/TheCraigHewitt/seomachine)
> A specialized Claude Code workspace for creating long-form, SEO-optimized blog content for any business. This system helps you research, write, analyze, and optimize content that ranks well and serves your target audience.

**Language:** Python  |  **Stars:** 3,755  |  **Forks:** 646  |  **Score:** 3,352  |  **Created:** 2025-10-29

**Background:** SEO Machine is a specialized Claude Code workspace for creating long-form, SEO-optimized blog content. With over 3,700 stars, it provides custom commands, specialized agents, and 26 marketing skills covering copywriting, CRO, A/B testing, email sequences, and pricing strategy.

**Problem it solves:** Creating SEO-optimized content that actually ranks requires keyword research, search intent analysis, readability optimization, internal linking strategy, and meta element creation — tasks that content writers often handle manually or with disconnected tools. SEO Machine integrates all these capabilities into a single Claude Code workspace.

**Why another one?** SEO Machine's data integrations with Google Analytics 4, Google Search Console, and DataForSEO provide real-time performance insights that inform content strategy. The context-driven approach ensures brand voice and style guidelines are maintained across all generated content, and the workflow organization with structured directories keeps the content pipeline orderly.

---

## 18. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration

**Language:** TypeScript  |  **Stars:** 24,276  |  **Forks:** 2,718  |  **Score:** 3,347  |  **Created:** 2025-08-02

**Background:** GitNexus is a client-side knowledge graph creator that runs entirely in the browser, turning any GitHub repository or ZIP file into an interactive knowledge graph with a built-in Graph RAG agent. With over 24,000 stars, it provides deep code exploration capabilities without requiring any server infrastructure.

**Problem it solves:** Understanding a large codebase requires tracing dependencies, call chains, and execution flows across hundreds of files. Traditional code browsers show file trees but miss the relationships between components. GitNexus indexes every dependency and call chain into a navigable graph that reveals architectural patterns.

**Why another one?** GitNexus runs entirely client-side with zero server requirements, eliminating privacy concerns about uploading proprietary code. Its Graph RAG agent provides deeper analysis than description-based tools like DeepWiki — tracking every relationship in a knowledge graph rather than generating static summaries.

---

## 19. [Waza](https://github.com/tw93/Waza)
> 🥷 Engineering habits you already know, turned into skills Claude can run.

**Language:** Shell  |  **Stars:** 1,441  |  **Forks:** 74  |  **Score:** 3,268  |  **Created:** 2026-03-12

**Background:** Waza (meaning 'technique' in Japanese martial arts) by Tw93 packages engineering habits into Claude Code skills. With over 1,400 stars since its March 2026 launch, it focuses on the disciplined practices that distinguish skilled engineers — thinking before building, reviewing one's own work, debugging systematically, and writing clearly.

**Problem it solves:** AI makes developers faster but does not make them think more clearly, ship more carefully, or understand more deeply. The habits that separate good engineers from mediocre ones — requirement analysis, self-review, systematic debugging, interface design — are not encoded in typical AI workflows.

**Why another one?** Waza's philosophy is distinctive: each skill represents an engineering habit practiced until it becomes instinct, not a code generation template. The slash commands (/think, /design, /check) enforce deliberate practice within the AI-assisted workflow, ensuring speed does not come at the cost of engineering discipline.

---

## 20. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 26,562  |  **Forks:** 3,478  |  **Score:** 3,168  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is a self-improving AI agent with a built-in learning loop that creates skills from experience and builds a deepening model of who you are across sessions. With over 26,000 stars, it is the only agent that improves itself during use, nudging itself to persist knowledge and searching its own past conversations.

**Problem it solves:** AI agents start from zero in every session — they do not remember past interactions, learn from mistakes, or adapt to user preferences. This forces users to re-explain context repeatedly and prevents the agent from developing domain expertise over time.

**Why another one?** Hermes Agent's learning loop is its core differentiator: it creates skills from experience, improves them during use, and builds persistent user models across sessions. It runs on any infrastructure from a $5 VPS to a GPU cluster, supports 200+ models via OpenRouter, and operates across Telegram, Discord, Slack, WhatsApp, and Signal from a single gateway.

---

## 21. [immich](https://github.com/immich-app/immich)
> High performance self-hosted photo and video management solution.

**Language:** TypeScript  |  **Stars:** 96,610  |  **Forks:** 5,277  |  **Score:** 3,038  |  **Created:** 2022-02-03

**Background:** Immich is a high-performance, self-hosted photo and video management solution that has grown to over 96,000 stars. It provides a Google Photos-like experience with full control over data, supporting mobile apps, web interface, and automated backup workflows.

**Problem it solves:** Cloud photo services like Google Photos and iCloud require trusting third parties with personal media, offer limited storage without subscriptions, and can change terms or shut down at any time. Immich provides a self-hosted alternative with comparable performance and features, keeping all data under the user's control.

**Why another one?** Immich's performance and polish set it apart from other self-hosted alternatives. With mobile apps, facial recognition, map views, and machine learning-powered search, it delivers a consumer-grade experience on self-hosted infrastructure. The active community and frequent releases ensure it keeps pace with commercial offerings.

---

## 22. [METATRON](https://github.com/sooryathejas/METATRON)
> AI-powered penetration testing assistant using local LLM on linux (Parrot OS)

**Language:** Python  |  **Stars:** 1,265  |  **Forks:** 256  |  **Score:** 2,385  |  **Created:** 2026-04-02

**Background:** METATRON is a CLI-based AI penetration testing assistant that runs entirely on a local machine using a custom Qwen model via Ollama on Parrot OS Linux. Created just five days ago, it has already gained over 1,200 stars, reflecting interest in local, privacy-focused security tools.

**Problem it solves:** Penetration testing requires running multiple recon tools (nmap, whois, whatweb, nikto), interpreting their output, identifying vulnerabilities, and recommending exploits — a workflow that requires significant expertise. METATRON automates this by feeding tool output to a local AI that analyzes targets and suggests fixes.

**Why another one?** METATRON's fully local architecture — no cloud, no API keys, no subscriptions — makes it suitable for security-sensitive environments where sending scan data to external services is unacceptable. The agentic loop capability allows the AI to request additional tool runs mid-analysis, enabling deeper investigation without manual intervention.

---

## 23. [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
> Skill that audits and rewrites content to remove AI writing patterns. Use it with your favorite agents including Claude Code, OpenClaw, and Hermes.

**Language:** N/A  |  **Stars:** 196  |  **Forks:** 13  |  **Score:** 2,370  |  **Created:** 2026-03-06

**Background:** Avoid AI Writing is a portable skill for Claude Code, OpenClaw, Hermes, and other agentskills.io-compatible agents that audits and rewrites content to remove AI writing patterns ('AI-isms'). Despite having only 196 stars, its trending position reflects growing awareness of the problem of detectable AI-generated text.

**Problem it solves:** AI-generated content follows recognizable patterns — phrases like 'certainly,' 'moreover,' 'nestled in,' 'watershed moment' — that make text immediately identifiable as machine-written. This is problematic for professional content that needs to read as authentically human-authored.

**Why another one?** The skill operates in two modes: rewrite (flags and fixes patterns with a built-in second pass) and detect-only (flags patterns without altering text). Its cross-platform compatibility with multiple agents and the lightweight skill-based distribution make it easy to integrate into any writing workflow.

---

## 24. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**Language:** Python  |  **Stars:** 60,341  |  **Forks:** 5,996  |  **Score:** 2,335  |  **Created:** 2025-11-30

**Background:** UI UX Pro Max is an AI skill providing design intelligence for building professional UI/UX across multiple platforms and frameworks. With over 60,000 stars and 161 reasoning rules covering 67 UI styles, it is one of the most popular design-focused AI skills in the ecosystem.

**Problem it solves:** AI coding agents produce functional but visually generic interfaces because they lack design reasoning capabilities. They default to standard component libraries without considering visual hierarchy, spacing rhythm, color theory, or platform-specific design conventions.

**Why another one?** With 161 reasoning rules and 67 UI styles, UI UX Pro Max provides unusually deep design coverage compared to simpler prompt-based approaches. The Python CLI (uipro-cli) and npm distribution make it accessible across development environments, and the skill format ensures it works with any compatible AI coding agent.

---

## 25. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript in-page GUI agent. Control web interfaces with natural language.

**Language:** TypeScript  |  **Stars:** 16,171  |  **Forks:** 1,288  |  **Score:** 2,308  |  **Created:** 2025-09-23

**Background:** Page Agent by Alibaba is an in-page JavaScript GUI agent that controls web interfaces using natural language. With over 16,000 stars, it takes a unique approach by running entirely within the web page itself — no browser extension, no Python, no headless browser required.

**Problem it solves:** Web automation traditionally requires heavyweight setups: browser extensions with special permissions, Python scripts with Selenium or Playwright, or headless browser infrastructure. These approaches are complex to set up, fragile to maintain, and often blocked by content security policies.

**Why another one?** Page Agent's text-based DOM manipulation eliminates the need for screenshots or multi-modal LLMs, reducing both cost and latency. The in-page JavaScript approach means it works with any LLM provider and requires no special permissions. An optional Chrome extension extends capabilities to multi-page tasks when needed.

---

> **Day's theme:** The AI agent ecosystem is maturing rapidly, with today's trending repos dominated by specialized skills, structured development workflows, and tools that encode senior engineering practices into reusable agent capabilities. From job search automation to penetration testing, knowledge graph generation to design system files, the trend is clear: developers are moving beyond generic AI chat toward purpose-built agent workflows that enforce discipline, maintain quality, and solve specific domain problems. The prominence of Claw Code (173K stars in 8 days) and Superpowers (138K stars) signals that the community is converging on standardized agent harnesses and skill frameworks as the foundational layer for AI-assisted development.
