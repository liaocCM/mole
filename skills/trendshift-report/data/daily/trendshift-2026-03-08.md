# Trendshift Report — 2026-03-08
**Total:** 25 repositories

---

## 1. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies

**Language:** TypeScript  |  **Stars:** 9,517  |  **Forks:** 1,062  |  **Score:** 5,842  |  **Created:** 2026-03-02

**Background:** Paperclip is an open-source business orchestration platform that launched in early March 2026 and racked up nearly 10,000 stars in under a week. It aims to automate entire business operations by coordinating AI agents across departments — sales, support, finance, and logistics — without requiring human intervention in the loop.

**Problem it solves:** Running a small business involves juggling dozens of operational tools and manual handoffs between them. Paperclip provides a unified orchestration layer where AI agents handle these end-to-end workflows autonomously, from customer acquisition through fulfillment, removing the need for a human operator at each step.

**Why another one?** While agent frameworks like CrewAI and AutoGen focus on multi-agent task execution, Paperclip targets full business process automation rather than developer-facing agent orchestration. The "zero-human company" framing positions it as infrastructure for AI-native businesses, not just a developer tool for building chatbots or code assistants.

---

## 2. [ironclaw](https://github.com/nearai/ironclaw)
> IronClaw is OpenClaw inspired implementation in Rust focused on privacy and security

**Language:** Rust  |  **Stars:** 8,629  |  **Forks:** 908  |  **Score:** 5,714  |  **Created:** 2026-02-03

**Background:** IronClaw is a Rust reimplementation of the OpenClaw personal AI assistant, built by Near AI. Launched in early February 2026, it prioritizes privacy and security by leveraging Rust's memory safety guarantees and a local-first architecture. The project supports multiple languages and platforms, with dual MIT/Apache-2.0 licensing.

**Problem it solves:** OpenClaw is written in TypeScript and runs on Node.js, which introduces a large dependency surface area and runtime overhead. IronClaw provides the same personal assistant functionality with lower memory usage, faster startup, and fewer potential security vulnerabilities by virtue of Rust's compile-time safety guarantees.

**Why another one?** The Rust implementation offers a meaningfully different security profile. Memory-safe by default, no garbage collector pauses, and a smaller binary footprint make it attractive for users who want to run a personal AI assistant on constrained hardware or in environments where security auditing of the runtime matters.

---

## 3. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.

**Language:** —  |  **Stars:** 33,181  |  **Forks:** 3,144  |  **Score:** 4,071  |  **Created:** 2026-01-25

**Background:** Maintained by the VoltAgent team, this repository catalogs over 5,400 community-built skills for the OpenClaw personal AI assistant, organized by category. It draws from the official OpenClaw Skills Registry and applies filtering and categorization to make discovery practical. The project has grown to over 33,000 stars since its January 2026 launch.

**Problem it solves:** The official OpenClaw Skills Registry is a flat listing that becomes unwieldy at scale. This curated collection organizes skills by functional category — development, productivity, creativity, data analysis — making it possible to find relevant skills without scrolling through thousands of entries.

**Why another one?** It keeps trending because the OpenClaw ecosystem is expanding rapidly, and new skills are added daily. The curation layer adds genuine value over the raw registry by filtering out low-quality or abandoned skills and maintaining category organization that the official registry does not provide.

---

## 4. [generative-ai](https://github.com/GoogleCloudPlatform/generative-ai)
> Sample code and notebooks for Generative AI on Google Cloud, with Gemini on Vertex AI

**Language:** Jupyter Notebook  |  **Stars:** 14,626  |  **Forks:** 3,912  |  **Score:** 4,046  |  **Created:** 2023-05-05

**Background:** Google Cloud Platform's official repository of notebooks, code samples, and demo applications for building generative AI workflows on Vertex AI. Originally launched in May 2023, it has been continuously updated to cover each new Gemini model release, most recently Gemini 3.1 Pro.

**Problem it solves:** Getting started with Gemini models on Vertex AI requires understanding APIs, authentication, prompt engineering patterns, and integration with GCP services. This repository provides tested, runnable notebooks that demonstrate each capability, reducing the onboarding time from documentation to working code.

**Why another one?** The Gemini 3.1 Pro launch is driving renewed traffic. As Google's official sample repository, it is the canonical starting point for developers adopting new Gemini capabilities, and each major model release triggers a new wave of attention.

---

## 5. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 289,626  |  **Forks:** 54,924  |  **Score:** 3,994  |  **Created:** 2025-11-24

**Background:** OpenClaw is the dominant open-source personal AI assistant platform, with nearly 290,000 stars making it one of the most-starred repositories on GitHub. Launched in November 2025, it runs on any OS and platform, with an extensible skills system and a distinctive lobster-themed brand identity. The project has built a massive ecosystem of community skills, integrations, and derivative projects.

**Problem it solves:** Commercial AI assistants lock users into specific platforms and limit customization. OpenClaw provides a fully self-hosted, extensible AI assistant that users own and control, with a plugin architecture that allows the community to build and share capabilities through a skills registry.

**Why another one?** OpenClaw is the incumbent, not the challenger. It trends continuously because its ecosystem generates a steady stream of new skills, forks, and derivative projects that all link back to the main repository. At nearly 290K stars, it has reached a self-sustaining level of visibility.

---

## 6. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything

**Language:** Python  |  **Stars:** 10,216  |  **Forks:** 1,069  |  **Score:** 3,821  |  **Created:** 2025-11-26

**Background:** MiroFish is a swarm intelligence prediction engine developed with backing from Shanda Group. It applies bio-inspired collective intelligence algorithms to make predictions across domains — financial markets, weather patterns, social trends — by aggregating signals from multiple lightweight agents that each contribute partial observations.

**Problem it solves:** Traditional prediction systems rely on single monolithic models that are expensive to train and brittle to distribution shifts. MiroFish distributes the prediction task across a swarm of simple agents, each processing a different signal or data source, then aggregates their outputs. This makes the system more robust to individual agent failures and easier to extend with new data sources.

**Why another one?** Most prediction frameworks in the AI space are either transformer-based forecasting models or classical ensemble methods. MiroFish takes a genuinely different approach by using swarm intelligence algorithms inspired by biological systems like fish schools and ant colonies, offering a novel architectural paradigm rather than an incremental improvement on existing approaches.

---

## 7. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash is all you need - A nano Claude Code-like agent, built from 0 to 1

**Language:** TypeScript  |  **Stars:** 24,497  |  **Forks:** 4,467  |  **Score:** 3,235  |  **Created:** 2025-06-29

**Background:** Created by shareAI-lab, this educational repository walks developers through building a Claude Code-like terminal agent from scratch. It demonstrates that the core agent loop — send messages to an LLM, check if it wants to use tools, execute those tools, loop — is fundamentally simple. The project is available in English, Chinese, and Japanese.

**Problem it solves:** Agentic coding tools like Claude Code can appear complex from the outside, but the underlying pattern is straightforward. This project demystifies the architecture by building a minimal implementation step by step, making the agent pattern accessible to developers who want to understand how these tools work or build their own.

**Why another one?** It is not a competing product but an educational resource. Its continued trending reflects ongoing developer interest in understanding the internals of agentic coding tools rather than just using them as black boxes.

---

## 8. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers.

**Language:** Shell  |  **Stars:** 18,396  |  **Forks:** 2,842  |  **Score:** 2,972  |  **Created:** 2025-10-13

**Background:** Agency Agents is a collection of pre-built AI agent personas created by Mark Sitarzewski, each designed as a specialized expert with a defined personality, process, and set of deliverables. The agents span roles like frontend development, community management, content creation, and quality assurance, and are distributed as shell scripts and prompt configurations.

**Problem it solves:** Setting up an effective AI agent for a specific role requires crafting detailed system prompts, defining workflows, and establishing output formats. Agency Agents provides ready-to-use role definitions that can be dropped into any LLM-based workflow, eliminating the prompt engineering effort for common professional functions.

**Why another one?** The value is in the breadth and specificity of the role definitions. Rather than a generic "you are a helpful assistant" prompt, each agent has a detailed persona with specific processes and deliverable templates. The collection approach — dozens of agents in one repository — makes it a one-stop resource for teams adopting agent-based workflows.

---

## 9. [symphony](https://github.com/openai/symphony)
> Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents.

**Language:** Elixir  |  **Stars:** 9,439  |  **Forks:** 653  |  **Score:** 2,693  |  **Created:** 2026-02-26

**Background:** Symphony is OpenAI's Elixir-based orchestration layer for Codex, their coding agent. It monitors project management boards (currently Linear) for tasks, spawns isolated Codex agents to implement each one, and reports back with CI status, PR review feedback, complexity analysis, and walkthrough videos. The project launched in late February 2026 as an engineering preview.

**Problem it solves:** Even with capable coding agents, someone still has to assign tasks, review outputs, and manage the handoff between human intent and agent execution. Symphony automates this management layer by treating project board tickets as work orders that agents autonomously claim, implement, and deliver as reviewed pull requests.

**Why another one?** Symphony is notable for being written in Elixir — unusual for AI infrastructure — which gives it strong concurrency primitives for managing multiple simultaneous agent runs. The "proof of work" approach, where agents provide CI results, code reviews, and demo videos alongside their PRs, addresses the trust gap that makes teams reluctant to let agents work unsupervised.

---

## 10. [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
> Claude Code Skills and 500+ agent skills from official dev teams and the community, compatible with Codex, Antigravity, Gemini CLI, Cursor and others.

**Language:** —  |  **Stars:** 10,076  |  **Forks:** 875  |  **Score:** 2,629  |  **Created:** 2025-10-28

**Background:** Also maintained by VoltAgent, this companion repository to awesome-openclaw-skills catalogs over 500 agent skills that work across multiple coding agent platforms — Claude Code, Codex, Antigravity, Gemini CLI, and Cursor. It includes skills from official development teams as well as community contributions.

**Problem it solves:** The agent skills ecosystem is fragmented across platforms, with skills written for Claude Code not always compatible with Codex or Cursor. This repository collects and tags cross-compatible skills, helping developers find capabilities that work regardless of which coding agent they use.

**Why another one?** While awesome-openclaw-skills focuses exclusively on the OpenClaw ecosystem, this repository covers the broader landscape of coding agent skills. Its cross-platform compatibility tagging is the primary differentiator, serving developers who work with multiple agent tools.

---

## 11. [ui](https://github.com/shadcn-ui/ui)
> A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks.

**Language:** TypeScript  |  **Stars:** 108,588  |  **Forks:** 8,067  |  **Score:** 2,572  |  **Created:** 2023-01-04

**Background:** shadcn/ui is a component library and code distribution platform created by shadcn that provides beautifully designed, accessible UI components. Unlike traditional npm-installable component libraries, it uses a "copy into your project" distribution model where components are generated into your codebase and can be freely modified. It now supports multiple frameworks beyond its React origins.

**Problem it solves:** Traditional component libraries impose their styling opinions and upgrade cycles on consuming projects. By distributing source code instead of compiled packages, shadcn/ui gives developers full ownership of their components, eliminating version lock-in and enabling deep customization without fighting the library.

**Why another one?** shadcn/ui trends persistently because it has become the default component starting point for new web projects, especially those built with AI coding agents. Its v4 release and expansion to multiple frameworks continue to drive visibility, and its code-generation model aligns well with how coding agents scaffold projects.

---

## 12. [AFFiNE](https://github.com/toeverything/AFFiNE)
> There can be more than Notion and Miro. AFFiNE is a next-gen knowledge base that brings planning, sorting and creating all together.

**Language:** TypeScript  |  **Stars:** 65,229  |  **Forks:** 4,554  |  **Score:** 2,522  |  **Created:** 2022-07-31

**Background:** AFFiNE is an open-source knowledge base by toeverything that combines document editing, whiteboard drawing, and project planning in a single application. Positioned as a privacy-focused alternative to Notion and Miro, it uses a local-first architecture where data stays on the user's device by default, with optional cloud sync.

**Problem it solves:** Knowledge workers currently split their workflow across multiple tools — Notion for documents, Miro for visual brainstorming, and project management software for planning. AFFiNE unifies these into a single hyper-fused workspace, eliminating the context switching and data fragmentation that comes from using separate applications.

**Why another one?** The local-first, privacy-focused architecture differentiates it from Notion (cloud-native) and the open-source nature differentiates it from Miro (proprietary). AFFiNE continues to trend as it adds features that close the gap with its commercial competitors while maintaining its privacy-first positioning.

---

## 13. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript in-page GUI agent. Control web interfaces with natural language.

**Language:** TypeScript  |  **Stars:** 2,399  |  **Forks:** 194  |  **Score:** 2,450  |  **Created:** 2025-09-23

**Background:** Page Agent is an in-page GUI automation agent from Alibaba that lets users control web interfaces using natural language commands. Unlike browser automation tools that operate through external drivers, Page Agent runs inside the page itself as a JavaScript library, directly manipulating the DOM based on natural language instructions.

**Problem it solves:** Browser automation with Selenium or Playwright requires writing brittle selectors that break when the UI changes. Page Agent uses vision-language models to understand the page layout and translate natural language instructions into DOM operations, making web automation more resilient to UI changes and accessible to non-developers.

**Why another one?** The in-page approach is architecturally distinct from tools like Playwright or browser-use that operate from outside the page. By running inside the JavaScript runtime, Page Agent has direct access to the application's state and event handlers, enabling more precise interactions than screenshot-based approaches.

---

## 14. [skills](https://github.com/openai/skills)
> Skills Catalog for Codex

**Language:** Python  |  **Stars:** 13,583  |  **Forks:** 762  |  **Score:** 2,309  |  **Created:** 2025-11-25

**Background:** This is OpenAI's official skills catalog for Codex, their coding agent. Skills are structured folders of instructions, scripts, and resources that Codex can discover and use to perform specific tasks. The repository hosts system skills that ship with Codex, curated community skills, and experimental skills in development.

**Problem it solves:** Without skills, coding agents rely entirely on their base training for task-specific knowledge. Skills package domain expertise — coding standards, deployment procedures, testing strategies — into discoverable, reusable bundles that agents can apply automatically when relevant, improving consistency and quality.

**Why another one?** As OpenAI's official catalog, it defines the skills standard for the Codex ecosystem. It trends alongside the broader agent skills movement, which is currently the dominant theme in AI developer tooling.

---

## 15. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:** —  |  **Stars:** 22,126  |  **Forks:** 1,817  |  **Score:** 2,304  |  **Created:** 2026-02-08

**Background:** Curated by Hesam Sheikh, this repository collects real-world use cases showing how people integrate OpenClaw into their daily lives. It features 36 documented use cases spanning productivity, health, education, and personal automation, with contributions from the open-source AI builders community.

**Problem it solves:** OpenClaw's skills registry tells you what the assistant can do, but not how real people are actually using it. This collection bridges that gap by documenting specific workflows and setups that community members have found valuable, providing inspiration and practical templates for new users.

**Why another one?** Use-case collections serve a different purpose than skills catalogs. While awesome-openclaw-skills lists capabilities, this repository tells stories about outcomes. It keeps trending because OpenClaw's user base is growing rapidly and new use cases are being discovered weekly.

---

## 16. [daytona](https://github.com/daytonaio/daytona)
> Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code

**Language:** TypeScript  |  **Stars:** 63,165  |  **Forks:** 5,072  |  **Score:** 2,286  |  **Created:** 2024-02-06

**Background:** Daytona provides secure, elastic infrastructure specifically designed for running AI-generated code. Originally launched in February 2024, it has evolved from a development environment manager into a sandboxed execution platform for code produced by AI agents, with over 63,000 stars reflecting strong adoption in the AI tooling ecosystem.

**Problem it solves:** AI-generated code is untrusted by default — running it on a developer's local machine or production infrastructure creates security risks. Daytona provides isolated, disposable execution environments where AI-generated code can run safely, with resource limits and network controls that prevent malicious or buggy code from causing damage.

**Why another one?** Daytona's pivot to AI-generated code execution positions it uniquely in the market. While container services like Docker provide isolation, Daytona adds the orchestration layer specifically tuned for AI agent workflows — rapid environment provisioning, resource elasticity, and integration with coding agent platforms.

---

## 17. [terraink](https://github.com/yousifamanuel/terraink)
> TerraInk: The Cartographic Poster Engine that creates unique and customizable map posters

**Language:** TypeScript  |  **Stars:** 891  |  **Forks:** 84  |  **Score:** 2,104  |  **Created:** 2026-02-10

**Background:** TerraInk is a web-based cartographic poster engine that generates customizable map posters from geographic data. Users select a location, choose from style presets, and produce print-ready poster artwork. The project launched in February 2026 and is available both as a hosted service at terraink.app and as self-hostable open-source code.

**Problem it solves:** Custom map posters are typically produced by commercial services that charge premium prices and offer limited customization. TerraInk makes the entire poster generation pipeline open-source, allowing users to create personalized map art for any location with full control over colors, typography, and layout.

**Why another one?** TerraInk is a niche creative tool rather than another AI framework. It stands out in a trending list dominated by agent tooling as a focused, well-designed product that solves a specific creative need. The self-hosting option and open-source availability differentiate it from commercial alternatives like Mapiful.

---

## 18. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
> LLM-driven A/H/US stock intelligent analyzer with multi-source data, real-time news, Gemini dashboard, and multi-channel push notifications

**Language:** Python  |  **Stars:** 17,898  |  **Forks:** 18,310  |  **Score:** 2,083  |  **Created:** 2026-01-10

**Background:** This Chinese-language project provides an automated stock analysis system that combines multiple data sources, real-time news feeds, and Gemini-powered analysis dashboards. It runs on GitHub Actions for zero-cost scheduled execution and pushes analysis results through multiple notification channels. The project covers A-shares, H-shares, and US markets.

**Problem it solves:** Individual investors struggle to process the volume of market data and news required for informed trading decisions. This system automates the data collection, analysis, and notification pipeline, delivering LLM-generated market intelligence on a schedule without requiring any infrastructure investment.

**Why another one?** The zero-cost architecture using GitHub Actions for scheduling and free-tier LLM APIs for analysis removes the barrier to entry entirely. Most comparable tools require a server or paid API keys. The multi-market coverage (A/H/US) also makes it uniquely useful for Chinese investors with cross-market exposure.

---

## 19. [Siftly](https://github.com/viperrcrypto/Siftly)
> Local Twitter/X bookmark organizer with AI categorization and mindmap visualization

**Language:** TypeScript  |  **Stars:** 1,279  |  **Forks:** 102  |  **Score:** 2,080  |  **Created:** 2026-03-04

**Background:** Siftly is a self-hosted Twitter/X bookmark manager that uses AI to automatically categorize saved bookmarks and visualize them as interactive mindmaps. Built with Next.js 16, TypeScript, and SQLite, it runs entirely locally with no cloud dependency. The project launched in early March 2026.

**Problem it solves:** Twitter/X bookmarks are a flat, unsearchable list that grows unbounded. Most users save hundreds of bookmarks and never revisit them because there is no organization or discovery layer. Siftly imports bookmarks, categorizes them with AI, and provides search and mindmap visualization to make the collection useful.

**Why another one?** The mindmap visualization is the distinguishing feature. Other bookmark managers organize content into folders or tags, but Siftly maps relationships between bookmarks visually, helping users discover thematic connections they did not explicitly create.

---

## 20. [free-for-dev](https://github.com/ripienaar/free-for-dev)
> A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev

**Language:** HTML  |  **Stars:** 119,167  |  **Forks:** 12,312  |  **Score:** 2,079  |  **Created:** 2015-03-18

**Background:** Maintained by R.I. Pienaar since March 2015, free-for-dev is one of the longest-running community-curated lists on GitHub. It catalogs SaaS, PaaS, and IaaS services with free tiers relevant to developers and DevOps engineers. Over 1,600 contributors have shaped its contents across more than a decade of maintenance.

**Problem it solves:** Finding services with genuinely useful free tiers requires checking individual pricing pages across hundreds of providers. This list aggregates and categorizes them in one place, saving developers hours of research when bootstrapping projects or looking for cost-free alternatives.

**Why another one?** It is not another one — it is the original and remains the definitive resource. It trends periodically as developers share it with new cohorts and as the list is updated with new services. At nearly 120,000 stars, it has established itself as essential developer infrastructure.

---

## 21. [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
> An AI Hedge Fund Team

**Language:** Python  |  **Stars:** 47,031  |  **Forks:** 8,174  |  **Score:** 2,074  |  **Created:** 2024-11-29

**Background:** AI Hedge Fund is an educational proof-of-concept that simulates a multi-agent hedge fund team. It employs agents modeled after famous investors — Aswath Damodaran, Ben Graham, Bill Ackman, Cathie Wood, Charlie Munger — each applying their distinctive investment philosophy to analyze stocks and generate trading signals.

**Problem it solves:** Understanding how different investment philosophies lead to different conclusions on the same stock is typically learned through years of study and experience. This project makes those frameworks executable, allowing users to see how a value investor and a growth investor would analyze the same opportunity differently.

**Why another one?** The persona-based multi-agent approach is the differentiator. Rather than building a single trading algorithm, AI Hedge Fund creates a committee of agents with conflicting investment philosophies, producing a richer and more nuanced analysis than any single model could provide.

---

## 22. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster.

**Language:** Shell  |  **Stars:** 75,677  |  **Forks:** 6,100  |  **Score:** 2,061  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official terminal-based agentic coding tool. It understands full codebase context and executes development tasks — code generation, refactoring, git workflows — through natural language commands. It supports extensions via a skills and hooks system and can be used in terminals, IDEs, or through GitHub mentions.

**Problem it solves:** Developers spend significant time on repetitive tasks, codebase navigation, and version control management. Claude Code automates these directly in the terminal, eliminating context-switching between AI chat interfaces and development environments.

**Why another one?** Claude Code is Anthropic's first-party agent and a foundational component of the skills ecosystem that dominates this week's trending list. Its presence alongside multiple skills catalogs and agent frameworks reflects its role as a platform that other projects build upon.

---

## 23. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**Language:** JavaScript  |  **Stars:** 69,024  |  **Forks:** 8,618  |  **Score:** 2,052  |  **Created:** 2026-01-18

**Background:** Everything Claude Code (ECC) is a comprehensive performance optimization system for AI coding agents, started by Affaan in January 2026. It provides skills, instincts, memory management, and security configurations that work across Claude Code, Codex, OpenCode, and Cursor. The project has grown to nearly 70,000 stars and offers npm packages for easy installation.

**Problem it solves:** Out-of-the-box coding agents lack opinionated configurations for research-first development, security hardening, and persistent memory across sessions. ECC bundles these optimizations into installable packages, transforming a generic coding agent into a tuned development partner.

**Why another one?** ECC takes a holistic approach rather than providing individual skills. It includes instinct-level behavioral modifications (how the agent approaches problems), not just task-specific skills. The cross-agent compatibility and npm distribution model also lower the adoption barrier compared to manually configuring each agent.

---

## 24. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 75,000  |  **Forks:** 5,793  |  **Score:** 1,950  |  **Created:** 2025-10-09

**Background:** Superpowers is Jesse Vincent's composable skills framework and structured development methodology for coding agents. It enforces a multi-phase workflow: spec extraction through conversation, chunked design review, detailed implementation planning, subagent-driven development, and two-stage code review. It works across Claude Code, Cursor, Codex, and OpenCode.

**Problem it solves:** Coding agents left to their default behavior tend to start writing code immediately without planning, skip tests, and drift from the original intent. Superpowers installs mandatory checkpoints — spec approval, plan review, TDD enforcement — that keep agents productive during extended autonomous sessions.

**Why another one?** Superpowers is a methodology, not a tool. It does not replace any coding agent but layers a disciplined workflow on top of whichever agent the developer uses. Its cross-platform compatibility and 75,000-star community validate the approach of treating agent workflow design as a first-class concern.

---

## 25. [system-design-primer](https://github.com/donnemartin/system-design-primer)
> Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards.

**Language:** Python  |  **Stars:** 338,012  |  **Forks:** 54,751  |  **Score:** 1,784  |  **Created:** 2017-02-26

**Background:** Created by Donne Martin in February 2017, system-design-primer is the most comprehensive open-source guide to system design interview preparation. It covers fundamental concepts like scalability, load balancing, caching, and database design through structured learning paths with Anki flashcards for spaced repetition. At over 338,000 stars, it is one of the most-starred repositories on GitHub.

**Problem it solves:** System design interviews are notoriously difficult to prepare for because the material is scattered across blog posts, papers, and engineering talks. This repository consolidates the essential knowledge into a structured curriculum with visual diagrams, real-world examples, and flashcards.

**Why another one?** It is the canonical resource, not a new entrant. It trends periodically as new cohorts of engineers begin interview preparation cycles. Its longevity — nine years of continuous maintenance — and comprehensive scope keep it relevant against newer alternatives.

---

> **Day's theme:** The AI agent ecosystem is crystallizing around skills, orchestration, and specialized personas — from business automation and investment analysis to coding workflow methodologies — as the community shifts from building individual agents to building the infrastructure that makes agents work together.
