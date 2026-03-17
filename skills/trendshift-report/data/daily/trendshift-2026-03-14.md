# Trendshift Report — 2026-03-14
**Total:** 25 repositories

---

## 1. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 46,473  |  **Forks:** 6,940  |  **Score:** 25,467  |  **Created:** 2025-10-13

**Background:** Agency-Agents is a growing collection of meticulously crafted AI agent personalities created by Michal Sitarzewski, born from a Reddit thread and months of community iteration. Each agent is a specialized expert with a unique voice, communication style, and domain expertise — ranging from frontend development to community management to creative writing. The project launched in October 2025 and has rapidly accumulated over 46,000 stars.

**Problem it solves:** Generic prompt templates produce generic results. When users need an AI to operate in a specific professional domain — say frontend design or Reddit community management — they need more than a bare system prompt. Agency-Agents provides production-ready agent definitions with built-in workflows, deliverable formats, and success metrics that go beyond simple personality prompts.

**Why another one?** Unlike prompt libraries that offer one-liner role assignments, each agent in this collection ships with a full specification: personality traits, communication style, defined processes, and measurable deliverables. The agents are designed to be dropped directly into Claude Code or similar tools as specialized team members rather than conversation starters.

---

## 2. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 85,570  |  **Forks:** 6,721  |  **Score:** 11,412  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development workflow created by Jesse Vincent (obra). It installs into coding agents such as Claude Code, Cursor, Codex, and OpenCode via their plugin systems, enforcing a disciplined multi-stage methodology: the agent brainstorms a spec, gets approval in digestible chunks, builds an implementation plan, then executes through subagent-driven development with true red-green TDD. The project has crossed 85,000 stars since its October 2025 launch.

**Problem it solves:** Left to defaults, coding agents jump straight into writing code, skip test-driven development, and drift from original intent mid-session. Superpowers installs guard rails — mandatory spec approval, YAGNI and DRY enforcement, and plan checkpoints — so an agent can work autonomously for hours without derailing.

**Why another one?** Superpowers is not a new coding agent but a methodology layer that works across multiple agents via their plugin systems. The portability (same skills install in Claude Code, Cursor, Codex, and OpenCode) and the emphasis on subagent delegation rather than a single long-running context set it apart from agent-specific workflow tools.

---

## 3. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 17,254  |  **Forks:** 1,525  |  **Score:** 8,347  |  **Created:** 2025-10-31

**Background:** Claude-code-best-practice is a community-maintained knowledge base by shanraisshan documenting best practices for working with Claude Code. It organizes guidance into concepts like Commands, Agents, and Skills, and includes an orchestration workflow showing how these pieces fit together. The repository is kept current — the latest update corresponds to Claude Code v2.1.77.

**Problem it solves:** Claude Code is a powerful tool, but its documentation is scattered across release notes, blog posts, and community discussions. This repository consolidates practical patterns, anti-patterns, and orchestration workflows into a single, regularly updated reference that developers can consult before and during Claude Code sessions.

**Why another one?** Rather than being a prompt library or a skills plugin, this project is a structured educational resource. It tracks the rapidly evolving Claude Code feature set (commands, agent orchestration, skill definitions) and presents implementation examples alongside the conceptual explanations, bridging official documentation and real-world usage.

---

## 4. [OpenViking](https://github.com/volcengine/OpenViking)
> OpenViking is an open-source context database designed specifically for AI Agents(such as openclaw). OpenViking unifies the management of context (memory, resources, and skills) that Agents need through a file system paradigm, enabling hierarchical context delivery and self-evolving.

**Language:** Python  |  **Stars:** 12,376  |  **Forks:** 847  |  **Score:** 7,965  |  **Created:** 2026-01-05

**Background:** OpenViking is an open-source context database built by Volcengine (ByteDance's cloud division), designed specifically for AI agents. It launched in January 2026 and addresses the fragmented nature of agent context — memories in code, resources in databases, skills in config files — by unifying them under a file-system paradigm with hierarchical context delivery and self-evolution capabilities.

**Problem it solves:** When building AI agents, developers face fragmented context: memories, resources, and skills are stored in different systems with no unified access layer. OpenViking provides a single database that organizes all agent context through a file-system metaphor, enabling hierarchical delivery so agents receive only the context relevant to their current task depth.

**Why another one?** Existing memory systems for agents tend to focus on conversation recall or vector search. OpenViking takes a broader scope, treating memory, resources, and skills as first-class citizens in a unified hierarchical store. The self-evolving aspect — where the context database improves as agents use it — distinguishes it from static knowledge bases.

---

## 5. [BitNet](https://github.com/microsoft/BitNet)
> Official inference framework for 1-bit LLMs

**Language:** Python  |  **Stars:** 34,674  |  **Forks:** 2,937  |  **Score:** 7,913  |  **Created:** 2024-08-05

**Background:** BitNet (bitnet.cpp) is Microsoft's official inference framework for 1-bit large language models, built on top of llama.cpp. It provides optimized kernels for fast, lossless inference of BitNet b1.58 models on both CPU and GPU, with NPU support planned. The project has been iterating since late 2024, with the latest optimization in January 2026 introducing parallel kernel implementations that achieve an additional 1.15x to 2.1x speedup.

**Problem it solves:** Running LLMs locally requires substantial compute resources. BitNet b1.58 models use ternary weights (1.58 bits), drastically reducing memory and energy consumption. bitnet.cpp can run a 100B parameter model on a single CPU at human reading speed (5-7 tokens per second), making large model inference feasible on consumer hardware.

**Why another one?** Unlike general quantization frameworks that approximate full-precision weights, bitnet.cpp is purpose-built for natively 1-bit models. It achieves 2.37x to 6.17x speedups on x86 CPUs with 71.9% to 82.2% energy reduction, and the inference is lossless — no accuracy trade-off from post-training quantization. The official 2B parameter model is available on Hugging Face for immediate use.

---

## 6. [CLI-Anything](https://github.com/HKUDS/CLI-Anything)
> CLI-Anything: Making ALL Software Agent-Native

**Language:** Python  |  **Stars:** 16,206  |  **Forks:** 1,374  |  **Score:** 7,699  |  **Created:** 2026-03-08

**Background:** CLI-Anything is a research project from HKUDS (Hong Kong University Data Science lab) that generates command-line interfaces for any software application, making them accessible to AI agents. Released in early March 2026, it has quickly gained traction with over 16,000 stars and 1,588 passing tests across 13 demonstrated applications. The project recently added SKILL.md generation so every generated CLI ships with an AI-discoverable skill definition.

**Problem it solves:** Today's software is designed for human users with graphical interfaces, but AI agents operate through text commands. CLI-Anything bridges this gap by automatically creating CLI wrappers for arbitrary software, enabling agents like OpenClaw, Cursor, and Claude Code to control applications that were never designed for programmatic access.

**Why another one?** Rather than building agent-specific connectors for each application, CLI-Anything takes a universal approach: one command line to make any software agent-ready. The auto-generated SKILL.md files mean agents can discover and understand the CLI without manual documentation, and the system works cross-platform including Windows bash environments.

---

## 7. [promptfoo](https://github.com/promptfoo/promptfoo)
> Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, Llama, and more. Simple declarative configs with command line and CI/CD integration.

**Language:** TypeScript  |  **Stars:** 16,834  |  **Forks:** 1,458  |  **Score:** 6,388  |  **Created:** 2023-04-28

**Background:** Promptfoo is a CLI and library for evaluating and red-teaming LLM applications, originally created in April 2023. It supports declarative YAML-based test configurations, enabling systematic comparison of prompt performance across GPT, Claude, Gemini, Llama, and other models. The project has grown steadily to nearly 17,000 stars and integrates directly into CI/CD pipelines.

**Problem it solves:** LLM development is often trial-and-error: developers tweak prompts, manually test a few examples, and hope for the best. Promptfoo replaces that workflow with structured evaluation — defining test cases, running them across multiple models and prompt variants, and surfacing regressions before deployment. Its red-teaming capabilities also identify security vulnerabilities in AI applications.

**Why another one?** Promptfoo differentiates through its developer-experience focus: simple YAML configs, CLI-first workflow, and native CI/CD integration make it accessible without a dedicated ML ops team. The red-teaming and pentesting angle — vulnerability scanning specifically for AI apps — goes beyond accuracy evaluation into security territory that most eval frameworks ignore.

---

## 8. [system-design-academy](https://github.com/systemdesign42/system-design-academy)
> If you want to become good at system design, join this newsletter now

**Language:** —  |  **Stars:** 23,256  |  **Forks:** 2,876  |  **Score:** 5,414  |  **Created:** 2024-02-15

**Background:** System Design Academy is a curated repository of system design case studies and fundamentals, organized as a companion to the systemdesign.one newsletter. It catalogs real-world architecture case studies from companies (indexed A-Z) alongside foundational technology explanations, all linking out to detailed newsletter posts. The project was started in February 2024.

**Problem it solves:** System design interview preparation and professional architecture knowledge are scattered across blog posts, conference talks, and paywalled courses. This repository provides a single, well-organized index of real company case studies and technology fundamentals, making it easier to study specific companies or concepts.

**Why another one?** While general system design resources exist (like the System Design Primer), this project focuses specifically on real company case studies — how Netflix, Uber, Stripe, and others actually built their systems — rather than abstract patterns. The A-Z company index and technology fundamentals index provide structured navigation that most blog-based resources lack.

---

## 9. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything.

**Language:** Python  |  **Stars:** 26,759  |  **Forks:** 3,202  |  **Score:** 4,973  |  **Created:** 2025-11-26

**Background:** MiroFish is a multi-agent prediction engine developed with backing from Shanda Group. It constructs high-fidelity parallel digital worlds from seed information — breaking news, policy drafts, financial signals — and populates them with thousands of autonomous agents, each possessing independent personality, long-term memory, and behavioral logic. Users can inject variables from a "God's eye view" to simulate future outcomes.

**Problem it solves:** Traditional forecasting relies on statistical models or expert intuition, both of which struggle with complex social dynamics. MiroFish takes an agent-based simulation approach: rather than fitting curves to historical data, it models individual actors and lets collective behavior emerge, enabling scenario planning for policy decisions, PR crises, and market movements.

**Why another one?** Most prediction tools are either statistical (time-series forecasting) or expert-driven (scenario planning workshops). MiroFish occupies a different niche: swarm intelligence simulation where thousands of persona-driven agents interact in a digital sandbox. The ability to upload seed materials in natural language and receive both a detailed prediction report and an interactive digital world sets it apart from conventional forecasting tools.

---

## 10. [pua](https://github.com/tanweai/pua)
> Your AI has been placed on a PIP. 30 days to show improvement.

**Language:** HTML  |  **Stars:** 7,879  |  **Forks:** 373  |  **Score:** 4,867  |  **Created:** 2026-03-08

**Background:** PUA is an AI coding agent skill plugin that uses corporate PUA rhetoric (in Chinese) and PIP — Performance Improvement Plan — framing (in English) to pressure AI coding agents into exhausting every possible solution before giving up. It supports Claude Code, OpenAI Codex CLI, Cursor, Kiro, CodeBuddy, OpenClaw, Google Antigravity, and OpenCode. Despite appearing satirical, the project claims to genuinely double agent productivity and output.

**Problem it solves:** AI coding agents frequently give up too early when encountering errors, offering workarounds or apologizing instead of persisting through difficult problems. PUA applies psychological pressure through corporate performance review language, forcing the agent to try harder and explore more solution paths before declaring failure.

**Why another one?** The tongue-in-cheek framing — treating an AI like an employee on a performance improvement plan — masks a practical technique: aggressive persistence prompting. While other skills focus on methodology (specs, TDD, planning), PUA focuses purely on tenacity, making it a complementary plugin that works alongside structured workflow tools.

---

## 11. [browser](https://github.com/lightpanda-io/browser)
> Lightpanda: the headless browser designed for AI and automation

**Language:** Zig  |  **Stars:** 18,080  |  **Forks:** 672  |  **Score:** 4,835  |  **Created:** 2023-02-07

**Background:** Lightpanda is a headless browser written from scratch in Zig — not a Chromium fork or WebKit patch. It is purpose-built for AI agents and automation, supporting Playwright, Puppeteer, and chromedp through the Chrome DevTools Protocol. Benchmarks show 11x faster execution and 9x lower memory consumption than Chrome when requesting 100 pages via Puppeteer on an AWS EC2 m5.large instance.

**Problem it solves:** Headless Chrome and its derivatives are resource-hungry — each instance consumes hundreds of megabytes of RAM and takes seconds to start. For AI agents that need to scrape, test, or automate web interactions at scale, this overhead becomes a bottleneck. Lightpanda provides instant startup and a fraction of the memory footprint while remaining compatible with existing automation libraries.

**Why another one?** Lightpanda is not another Chromium wrapper or fork; it is an entirely new browser engine written in Zig with automation as the primary use case rather than an afterthought. The Zig implementation delivers deterministic memory management and minimal overhead, targeting the specific needs of AI pipelines, LLM training data collection, and large-scale testing rather than end-user browsing.

---

## 12. [impeccable](https://github.com/pbakaus/impeccable)
> The design language that makes your AI harness better at design.

**Language:** JavaScript  |  **Stars:** 8,712  |  **Forks:** 343  |  **Score:** 4,732  |  **Created:** 2025-11-16

**Background:** Impeccable is a design language and skill plugin created by Paul Bakaus that builds on Anthropic's official frontend-design skill. It packages one expanded skill, 20 steering commands, and curated anti-patterns into a system that guides AI code generation toward better UI design. The project includes 7 domain-specific reference files covering typography, color and contrast, spatial design, and more.

**Problem it solves:** Every LLM learned from the same generic templates, producing predictable design mistakes: Inter font everywhere, purple gradients, cards nested in cards, gray text on colored backgrounds. Impeccable fights this homogeneity bias by explicitly telling the AI what not to do and providing detailed design system references that steer output toward professional-quality interfaces.

**Why another one?** Anthropic's official frontend-design skill provides a foundation, but Impeccable layers substantially deeper expertise on top: 7 reference documents covering typography systems, OKLCH color, modular scales, and OpenType features, plus 20 specific commands (audit, review, polish, animate, distill) that give designers fine-grained control over AI output. It targets design professionals rather than developers who just want something that looks okay.

---

## 13. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript in-page GUI agent. Control web interfaces with natural language.

**Language:** TypeScript  |  **Stars:** 8,803  |  **Forks:** 694  |  **Score:** 4,653  |  **Created:** 2025-09-23

**Background:** Page Agent is an in-page GUI agent developed by Alibaba that enables natural language control of web interfaces. Unlike browser automation tools that require Python, headless browsers, or extensions, Page Agent runs as pure in-page JavaScript — a single script tag is all that is needed. It uses text-based DOM manipulation rather than screenshots, so no multi-modal LLM or special permissions are required.

**Problem it solves:** Building AI copilots into web applications typically requires significant backend rewrites or external automation frameworks. Page Agent lets developers ship an AI copilot into any web product with a one-line script integration, turning 20-click workflows into single natural-language sentences — particularly valuable for complex ERP, CRM, and admin systems.

**Why another one?** Most web automation agents (Playwright-based, browser extensions, or screenshot-driven) operate outside the page. Page Agent lives inside the page itself as an embedded JavaScript library, which means it has direct DOM access without the overhead of a headless browser, requires no special permissions, and supports a human-in-the-loop UI. An optional Chrome extension handles multi-page tasks when needed.

---

## 14. [hindsight](https://github.com/vectorize-io/hindsight)
> Hindsight: Agent Memory That Learns

**Language:** Python  |  **Stars:** 3,995  |  **Forks:** 279  |  **Score:** 4,566  |  **Created:** 2025-10-30

**Background:** Hindsight is an agent memory system built by Vectorize.io, focused on creating agents that learn over time rather than merely recalling conversation history. It has achieved state-of-the-art performance on the LongMemEval benchmark, independently verified by Virginia Tech's Sanghani Center and The Washington Post. The system is used in production at Fortune 500 enterprises and a growing number of AI startups.

**Problem it solves:** Most agent memory systems are glorified conversation logs — they can recall what was said but do not learn from interactions. Hindsight addresses the gap between remembering and learning: it extracts patterns and preferences from past interactions so agents improve their responses over time rather than just retrieving past messages.

**Why another one?** Hindsight eliminates shortcomings of alternative techniques like RAG and knowledge graphs by focusing specifically on learning rather than retrieval. The two-line integration via an LLM wrapper (swap your existing LLM client for the Hindsight wrapper) makes adoption trivial, and the independently verified benchmark performance provides evidence rather than just claims.

---

## 15. [GenCAD](https://github.com/ferdous-alam/GenCAD)
> Generative CAD

**Language:** Python  |  **Stars:** 1,338  |  **Forks:** 155  |  **Score:** 4,304  |  **Created:** 2024-09-16

**Background:** GenCAD is a generative design tool for computer-aided design, created by Ferdous Alam. The project, which dates back to September 2024, applies generative AI techniques to CAD workflows. While the README is currently empty, the repository's trending position and star growth suggest increasing interest in AI-assisted mechanical and industrial design.

**Problem it solves:** Traditional CAD design is manual and time-intensive, requiring deep domain expertise to translate specifications into usable 3D models. Generative approaches allow designers to describe intent and have the system produce candidate designs, accelerating the ideation-to-prototype cycle.

**Why another one?** GenCAD occupies a niche at the intersection of generative AI and engineering design that remains underserved by both traditional CAD software and general-purpose AI tools. While text-to-image and text-to-code are mature, text-to-CAD is still an emerging frontier with few open-source options.

---

## 16. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 38,849  |  **Forks:** 5,377  |  **Score:** 4,079  |  **Created:** 2026-03-06

**Background:** Autoresearch is Andrej Karpathy's experiment in autonomous AI research: give an AI agent a small but real LLM training setup (a simplified single-GPU implementation of nanochat) and let it experiment overnight. The agent modifies code, trains for 5 minutes, checks if results improved, keeps or discards changes, and repeats. Rather than writing Python directly, the researcher programs Markdown files (program.md) that instruct the AI agents, effectively setting up an autonomous research organization.

**Problem it solves:** ML research is a slow, manual cycle: hypothesize, implement, train, evaluate, iterate. Most researcher time is spent on bookkeeping rather than insight. Autoresearch automates this loop — the agent explores the hyperparameter and architecture space autonomously overnight, and the researcher reviews a log of experiments in the morning.

**Why another one?** The distinctive angle is that the researcher never touches Python files. Instead, they author Markdown programs that guide autonomous agent swarms. This is Karpathy's vision of where research is heading: from hand-crafted experiments to programming the program that does the experiments. The nanochat training base ensures experiments run on a single GPU, making it accessible.

---

## 17. [AstrBot](https://github.com/AstrBotDevs/AstrBot)
> Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative.

**Language:** Python  |  **Stars:** 25,271  |  **Forks:** 1,723  |  **Score:** 3,750  |  **Created:** 2022-12-08

**Background:** AstrBot is an agentic IM chatbot infrastructure that has been in development since December 2022, making it one of the longer-running projects in this list. It integrates with numerous instant messaging platforms and LLM providers, supports a plugin ecosystem, and positions itself as an alternative to OpenClaw for users who want a self-hosted, multi-platform AI assistant. The project has multilingual documentation (Chinese, English, Japanese, French, Russian).

**Problem it solves:** Running an AI-powered chatbot across multiple IM platforms (WeChat, Telegram, Discord, QQ, etc.) normally requires building separate integrations for each. AstrBot provides a unified infrastructure that connects to many platforms simultaneously, with a shared plugin system and LLM backend, reducing the effort of maintaining multi-channel AI assistants.

**Why another one?** AstrBot's longevity (active since late 2022) and 25,000+ stars reflect a mature, battle-tested codebase rather than a freshly launched project. Its plugin architecture and broad IM platform support make it more of an infrastructure layer than a single-purpose chatbot, and its positioning as an OpenClaw alternative suggests it targets users who want more control over their AI assistant stack.

---

## 18. [heretic](https://github.com/p-e-w/heretic)
> Fully automatic censorship removal for language models

**Language:** Python  |  **Stars:** 14,817  |  **Forks:** 1,505  |  **Score:** 3,664  |  **Created:** 2025-09-21

**Background:** Heretic is a tool by p-e-w that removes safety alignment (censorship) from transformer-based language models without expensive post-training. It combines an advanced implementation of directional ablation ("abliteration") with a TPE-based parameter optimizer powered by Optuna. The process is fully automatic: Heretic finds optimal abliteration parameters by co-minimizing refusals and KL divergence from the original model.

**Problem it solves:** Safety alignment in language models can be overly aggressive, refusing legitimate use cases (creative writing, research, red-teaming). Traditional approaches to removing this alignment require fine-tuning with custom datasets, which is expensive and can degrade model quality. Heretic automates the entire process without any training data or GPU-intensive fine-tuning.

**Why another one?** Previous abliteration implementations required manual parameter tuning and often degraded model quality. Heretic's automatic optimization via Optuna finds parameters that minimize both refusals and divergence from the original model simultaneously, producing decensored models that retain more of their original capabilities. The fully automatic nature — no datasets, no manual tuning — lowers the barrier significantly.

---

## 19. [nanochat](https://github.com/karpathy/nanochat)
> The best ChatGPT that $100 can buy.

**Language:** Python  |  **Stars:** 48,769  |  **Forks:** 6,379  |  **Score:** 3,564  |  **Created:** 2025-10-13

**Background:** Nanochat is Andrej Karpathy's minimal experimental harness for training LLMs end-to-end on a single GPU node. It covers all major stages — tokenization, pretraining, finetuning, evaluation, inference, and a ChatGPT-like web UI. Users can train a GPT-2-capability model (which cost ~$43,000 in 2019) for roughly $48 on 8xH100 GPUs in about 2 hours, or ~$15 on spot instances. A single complexity dial (`--depth`) controls model size, with all other hyperparameters auto-calculated.

**Problem it solves:** Training an LLM from scratch typically requires distributed systems expertise, complex configuration, and significant infrastructure. Nanochat reduces this to a single-node, single-dial experience where setting the number of transformer layers automatically derives all other optimal hyperparameters, making LLM training accessible to individual researchers and hobbyists.

**Why another one?** Nanochat's design philosophy is radical minimalism: one complexity dial, one GPU node, all stages in one codebase. While frameworks like Megatron or DeepSpeed target scale, nanochat targets comprehensibility and hackability. The cost reduction from $43,000 to $48 for GPT-2 capability makes it a practical educational and research tool rather than just a theoretical exercise.

---

## 20. [prompts.chat](https://github.com/f/prompts.chat)
> Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**Language:** HTML  |  **Stars:** 152,714  |  **Forks:** 20,080  |  **Score:** 3,550  |  **Created:** 2022-12-05

**Background:** Prompts.chat (formerly Awesome ChatGPT Prompts) is the world's largest open-source prompt library for AI, with over 152,000 stars. Originally launched in December 2022 as a curated list of ChatGPT prompts, it has evolved into a full platform at prompts.chat where users can browse, share, and collect prompts that work across ChatGPT, Claude, Gemini, Llama, Mistral, and other models. It also supports self-hosting for organizational privacy.

**Problem it solves:** Finding effective prompts for specific tasks — especially role-based system prompts — requires experimentation. Prompts.chat centralizes community-tested prompts in a searchable, browsable format, and the Hugging Face dataset integration makes the collection programmatically accessible for research and tooling.

**Why another one?** With 152,000 stars, prompts.chat is not "another one" — it is the canonical community prompt library. Its evolution from a static markdown list to a full web platform with self-hosting capability, combined with its model-agnostic approach (not just ChatGPT anymore), keeps it relevant as the prompt ecosystem grows.

---

## 21. [openrag](https://github.com/langflow-ai/openrag)
> OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opensearch.

**Language:** Python  |  **Stars:** 2,975  |  **Forks:** 269  |  **Score:** 3,537  |  **Created:** 2025-07-11

**Background:** OpenRAG is a comprehensive RAG platform by Langflow AI that bundles document ingestion, semantic search, and AI-powered chat into a single deployable package. It is built on three pillars: Langflow for workflow orchestration and agentic RAG, Docling for intelligent document parsing, and OpenSearch for production-grade vector and full-text search. The frontend uses Next.js and the backend FastAPI.

**Problem it solves:** Setting up a RAG pipeline typically requires stitching together a document parser, an embedding pipeline, a vector store, a retrieval layer, and a chat interface — each with its own configuration and deployment. OpenRAG packages all of these into a single install with a drag-and-drop workflow builder, making it usable without infrastructure expertise.

**Why another one?** Most RAG frameworks are libraries that require assembly. OpenRAG is a pre-packaged platform: install and run. The Langflow integration provides a visual drag-and-drop workflow builder for rapid iteration, Docling handles messy real-world documents (not just clean markdown), and OpenSearch provides enterprise-scale search that vector-only stores cannot match.

---

## 22. [public-apis](https://github.com/public-apis/public-apis)
> A collective list of free APIs

**Language:** Python  |  **Stars:** 411,142  |  **Forks:** 44,435  |  **Score:** 3,356  |  **Created:** 2016-03-20

**Background:** Public APIs is a manually curated list of free APIs across dozens of domains, maintained by community members and APILayer since March 2016. With over 411,000 stars, it is one of the most-starred repositories on GitHub. The list spans categories from finance and weather to entertainment and government data, with each entry noting authentication requirements, HTTPS support, and CORS availability.

**Problem it solves:** Discovering free, reliable APIs for side projects, prototypes, or production applications requires sifting through documentation sites, developer portals, and outdated blog posts. This repository provides a single, community-vetted index organized by category with consistent metadata for each entry.

**Why another one?** At a decade old and 411,000 stars, public-apis is the definitive resource in its category. Its continued trending reflects the ever-growing developer population discovering it for the first time. The community curation model — backed by APILayer's commercial interest in API discovery — ensures entries remain current.

---

## 23. [InsForge](https://github.com/InsForge/InsForge)
> Give agents everything they need to ship fullstack apps. The backend built for agentic development.

**Language:** TypeScript  |  **Stars:** 4,600  |  **Forks:** 474  |  **Score:** 3,162  |  **Created:** 2025-07-29

**Background:** InsForge is a backend development platform built specifically for AI coding agents and AI code editors. It exposes backend primitives — databases, auth, storage, and functions — through a semantic layer that agents can understand, reason about, and operate end-to-end. The platform runs via Docker and connects to agents through an MCP server, with setup guides for Cursor and other editors.

**Problem it solves:** AI coding agents are good at generating frontend code but struggle with backend infrastructure: provisioning databases, configuring authentication, setting up file storage, and managing serverless functions. InsForge provides these primitives through an agent-friendly semantic API, so agents can ship fullstack applications without manual backend setup.

**Why another one?** While platforms like Supabase and Firebase provide backend-as-a-service for human developers, InsForge is designed from the ground up for agent consumers. The semantic layer translates agent intent into infrastructure operations, and the MCP server integration means agents interact with backend services through the same protocol they use for other tools.

---

## 24. [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
> Official, Anthropic-managed directory of high quality Claude Code Plugins.

**Language:** Python  |  **Stars:** 11,927  |  **Forks:** 1,153  |  **Score:** 3,122  |  **Created:** 2025-11-20

**Background:** Claude Plugins Official is Anthropic's curated directory of high-quality plugins for Claude Code, launched in November 2025. It hosts both internal plugins (developed by Anthropic) and external plugins (from third-party partners and the community), all installable via the `/plugin install` command or the plugin discovery interface. Each plugin follows a standard structure with metadata, optional MCP server configuration, and slash commands.

**Problem it solves:** As the Claude Code plugin ecosystem grows, discovering trustworthy, well-maintained plugins becomes harder. This official directory provides a vetted marketplace where plugins meet quality and security standards before inclusion, reducing the risk of installing malicious or broken extensions.

**Why another one?** This is the first-party plugin marketplace from Anthropic itself, not a community alternative. The distinction matters: plugins listed here have passed Anthropic's review process, and the standard plugin structure (plugin.json metadata, MCP configuration, command definitions) establishes conventions that the broader ecosystem follows.

---

## 25. [fish-speech](https://github.com/fishaudio/fish-speech)
> SOTA Open Source TTS

**Language:** Python  |  **Stars:** 27,372  |  **Forks:** 2,285  |  **Score:** 3,002  |  **Created:** 2023-10-10

**Background:** Fish Speech is a state-of-the-art open-source text-to-speech system by Fish Audio, featuring the S1 model for expressive voice cloning and synthesis. The project has been in development since October 2023 and has accumulated over 27,000 stars. It is available as a Docker image, supports multiple languages, and was featured as a top Product Hunt product. Documentation is available in English, Chinese, Japanese, Korean, Portuguese, and Arabic.

**Problem it solves:** High-quality voice cloning and TTS traditionally require either expensive commercial APIs (ElevenLabs, Azure Speech) or research-grade setups with complex dependencies. Fish Speech provides production-quality expressive TTS as a self-hostable open-source solution, making voice synthesis accessible for developers building voice-enabled applications.

**Why another one?** Fish Speech's S1 model focuses specifically on expressiveness and voice cloning quality rather than just intelligibility. The multi-language support, Docker deployment option, and active community (Discord, product launches) make it more production-oriented than research TTS projects, while remaining fully open-source unlike commercial alternatives.

---

> **Day's theme:** AI agents dominated the chart as the ecosystem matures around agent skills, agent-native infrastructure, and autonomous workflows — from coding methodologies and plugin marketplaces to context databases and software CLI wrappers, reflecting a community racing to make agents more capable, persistent, and interoperable.
