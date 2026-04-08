# Trendshift Report — 2026-03-26
**Total:** 25 repositories

---

## 1. [last30days-skill](https://github.com/mvanhorn/last30days-skill)
> AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

**Language:** Python  |  **Stars:** 18,665  |  **Forks:** 1,503  |  **Score:** 11,856  |  **Created:** 2026-01-23

**Background:** Last30Days is a Claude Code skill that researches any topic across Reddit, X, YouTube, Hacker News, Polymarket, and the broader web, then synthesizes a grounded summary of what happened in the past 30 days. Launched in late January 2026, it has quickly amassed over 18,000 stars by addressing a universal need: staying current in fast-moving domains.

**Problem it solves:** The AI world reinvents itself monthly, and manually tracking what the community is upvoting, sharing, betting on, and discussing across fragmented platforms is overwhelming. Last30Days automates multi-source research and delivers a synthesized, citation-backed summary in a single slash command.

**Why another one?** Unlike general-purpose search or RAG tools, Last30Days is purpose-built for recency — it exclusively targets the last 30 days of community discourse. Its multi-platform coverage (Reddit, X, YouTube, HN, Polymarket) provides a cross-validated view that no single-source tool can match, and its native Claude Code integration makes it a one-command operation.

---

## 2. [insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper)
> An opinionated CLI to transcribe Audio files w/ Whisper on-device! Powered by Transformers, Optimum & flash-attn

**Language:** Jupyter Notebook  |  **Stars:** 12,360  |  **Forks:** 907  |  **Score:** 9,376  |  **Created:** 2023-10-10

**Background:** Insanely Fast Whisper is an opinionated CLI tool that transcribes audio files using OpenAI's Whisper model on-device, powered by Hugging Face Transformers, Optimum, and flash-attention. Originally released in October 2023, it continues to trend with over 12,000 stars as demand for local speech-to-text processing grows.

**Problem it solves:** Transcribing audio with Whisper's large models is painfully slow on default configurations. Insanely Fast Whisper applies aggressive optimizations — flash-attention, batched inference, and hardware-specific tuning — to transcribe 150 minutes of audio in under 98 seconds on consumer hardware.

**Why another one?** The "opinionated" design philosophy is the differentiator. Rather than exposing every Whisper configuration knob, it ships sensible defaults that maximize speed out of the box. The CLI-first interface makes it trivially scriptable for batch processing, and on-device execution means no audio data leaves the user's machine.

---

## 3. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 135,699  |  **Forks:** 11,370  |  **Score:** 8,635  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, now surpassing 135,000 stars. It enforces a disciplined process: the agent teases out a spec, presents it in digestible chunks, builds an implementation plan, then launches subagent-driven development with built-in review cycles. It has become the de facto standard for structured agent-driven development.

**Problem it solves:** Coding agents left to their own devices jump straight into writing code without understanding the full problem. Superpowers enforces a structured spec-plan-implement-review workflow, ensuring agents work methodically through TDD and YAGNI principles rather than producing poorly planned implementations.

**Why another one?** Superpowers focuses on development methodology rather than tool orchestration. Its subagent-driven development model allows agents to work autonomously for hours without drifting from the plan. At 135,000 stars and growing, it has proven its approach at scale and continues to serve as the agentic development reference implementation.

---

## 4. [deer-flow](https://github.com/bytedance/deer-flow)
> An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.

**Language:** Python  |  **Stars:** 57,981  |  **Forks:** 7,218  |  **Score:** 6,214  |  **Created:** 2025-05-07

**Background:** DeerFlow 2.0 by ByteDance is a ground-up rewrite of their SuperAgent harness, combining research, coding, and creative capabilities into a single framework. With nearly 58,000 stars (up from 39,000 just three days ago), DeerFlow continues its explosive growth as the leading open-source long-horizon agent orchestration platform.

**Problem it solves:** Complex tasks that span research, code generation, and content creation require orchestrating multiple tools and maintaining context across long-running sessions. DeerFlow provides a unified harness with sandboxes, persistent memory, subagent spawning, and a message gateway to handle tasks ranging from minutes to hours autonomously.

**Why another one?** DeerFlow's backing by ByteDance provides sustained engineering investment — the 2.0 ground-up rewrite shares no code with v1, demonstrating serious commitment. The message gateway architecture enables multi-modal task handling, and the sandbox system provides safe execution environments that most competing frameworks lack.

---

## 5. [agentscope](https://github.com/agentscope-ai/agentscope)
> Build and run agents you can see, understand and trust.

**Language:** Python  |  **Stars:** 22,999  |  **Forks:** 2,370  |  **Score:** 5,301  |  **Created:** 2024-01-12

**Background:** AgentScope is a multi-agent framework focused on transparency and trust, backed by academic research (arXiv paper). With nearly 23,000 stars and over two years of active development, it has matured into a production-grade platform for building observable, debuggable agent systems.

**Problem it solves:** Most agent frameworks treat their internal state as a black box, making it impossible to understand why an agent made a particular decision or to trust its output in high-stakes scenarios. AgentScope makes agent behavior visible and auditable, enabling developers to build agents they can actually trust.

**Why another one?** The emphasis on observability and trust sets AgentScope apart from frameworks that prioritize raw capability. In enterprise and regulated environments where AI decisions must be explainable, AgentScope's transparent architecture is a requirement rather than a nice-to-have. Its academic foundation provides rigor that purely community-driven projects often lack.

---

## 6. [litellm](https://github.com/BerriAI/litellm)
> Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI format, with cost tracking, guardrails, loadbalancing and logging.

**Language:** Python  |  **Stars:** 42,143  |  **Forks:** 6,983  |  **Score:** 4,714  |  **Created:** 2023-07-27

**Background:** LiteLLM is an open-source AI Gateway that provides a unified OpenAI-compatible interface to over 100 LLM providers including Bedrock, Azure, Anthropic, VertexAI, and more. With 42,000 stars and nearly three years of development, it has become essential infrastructure for teams running multi-provider LLM deployments.

**Problem it solves:** Organizations using multiple LLM providers face fragmented SDKs, inconsistent APIs, and no unified way to track costs, enforce guardrails, or load-balance across providers. LiteLLM normalizes everything into the OpenAI format, providing a single integration point with built-in cost tracking, logging, and provider failover.

**Why another one?** LiteLLM's breadth of provider support (100+) and its dual deployment model — lightweight Python SDK for development, full proxy server for production — make it adaptable to any scale. The enterprise-ready features (guardrails, load balancing, cost tracking) go well beyond simple API translation.

---

## 7. [pua](https://github.com/tanweai/pua)
> A high-agency skill for AI coding agents. Double your Claude Code / Codex productivity and output.

**Language:** TypeScript  |  **Stars:** 14,970  |  **Forks:** 829  |  **Score:** 4,559  |  **Created:** 2026-03-08

**Background:** PUA (Performance Under Assessment) is a skill that applies corporate performance culture rhetoric to push AI coding agents to exhaust every possible approach before giving up. Released less than three weeks ago, it has already reached nearly 15,000 stars, reflecting widespread frustration with agents that give up too easily on difficult tasks.

**Problem it solves:** AI coding agents frequently abandon tasks prematurely, suggest manual workarounds, or loop on the same failed approach without trying alternatives. PUA intervenes when the agent is about to give up, applying systematic debugging methodology and motivational pressure to force thorough problem-solving.

**Why another one?** PUA takes a deliberately provocative approach — framing agent performance improvement as a corporate PIP (Performance Improvement Plan). This tongue-in-cheek style has driven viral adoption, but the underlying methodology is sound: systematic escalation from simple fixes to deep debugging, with forced exploration of alternative approaches.

---

## 8. [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> Turn Claude Code into a full game dev studio — 48 AI agents, 36 workflow skills, and a complete coordination system mirroring real studio hierarchy.

**Language:** Shell  |  **Stars:** 8,174  |  **Forks:** 1,230  |  **Score:** 4,502  |  **Created:** 2026-02-12

**Background:** Claude Code Game Studios by Donchitos transforms a single Claude Code session into a full game development studio with 49 specialized AI agents, 72 workflow skills, 12 hooks, and 11 rules. The coordination system mirrors a real studio hierarchy — from creative directors down to QA testers — organized into three tiers mapped to different model capabilities.

**Problem it solves:** Game development requires coordination across many disciplines — design, art, programming, audio, testing, and project management. A single AI agent cannot effectively context-switch between these roles. Game Studios provides dedicated agents for each role with workflows that enforce proper handoffs and review processes.

**Why another one?** The studio hierarchy metaphor is the key innovation. Rather than generic multi-agent orchestration, Game Studios maps directly to how real game studios operate with three-tier agent organization (Directors on Opus, Leads on Sonnet, Specialists on Sonnet/Haiku). The 49-agent, 72-skill scale goes well beyond proof-of-concept into production-grade complexity.

---

## 9. [supermemory](https://github.com/supermemoryai/supermemory)
> Memory engine and app that is extremely fast, scalable. The Memory API for the AI era.

**Language:** TypeScript  |  **Stars:** 21,191  |  **Forks:** 1,934  |  **Score:** 3,945  |  **Created:** 2024-02-27

**Background:** Supermemory is a state-of-the-art memory and context engine for AI, ranking first on LongMemEval, LoCoMo, and ConvoMem — the three major benchmarks for AI memory. With over 21,000 stars and two years of development, it provides the full context stack: memory extraction, user profiles, hybrid search, connectors, and multi-modal file processing.

**Problem it solves:** AI forgets everything between conversations. Supermemory fixes this by automatically learning from conversations, extracting facts, building user profiles, handling knowledge updates and contradictions, forgetting expired information, and delivering the right context at the right time — all through a single API.

**Why another one?** Supermemory's benchmark-leading performance across three major memory evaluations validates its approach. Unlike simpler memory tools, it handles temporal changes, contradictions, and automatic forgetting. The connector ecosystem (Google Drive, Gmail, Notion, OneDrive, GitHub) and plugin support for Claude Code and other agents make it a complete context platform.

---

## 10. [OpenSpace](https://github.com/HKUDS/OpenSpace)
> "OpenSpace: Make Your Agents: Smarter, Low-Cost, Self-Evolving" -- Community: https://open-space.cloud/

**Language:** Python  |  **Stars:** 3,846  |  **Forks:** 449  |  **Score:** 3,771  |  **Created:** 2026-03-24

**Background:** OpenSpace by the HKU Data Science lab is an agent optimization platform released just two days ago that has already accumulated 3,846 stars. It promises 46% fewer tokens, demonstrated $11K earned in 6 hours through optimized agent workflows, and features self-evolving skills with cross-agent experience sharing.

**Problem it solves:** AI agents are expensive to run and do not learn from past successes or failures. OpenSpace reduces token consumption by nearly half while enabling agents to evolve their skills autonomously and share effective strategies across agent instances, dramatically lowering costs and improving output quality.

**Why another one?** The self-evolving and experience-sharing capabilities distinguish OpenSpace from static agent frameworks. Rather than relying on manually crafted skills, agents using OpenSpace autonomously develop and refine their own approaches. The academic backing from HKU provides research rigor, and the dramatic cost reduction claims (46% fewer tokens) address the most pressing concern for production agent deployments.

---

## 11. [editor](https://github.com/pascalorg/editor)
> Create and share 3D architectural projects.

**Language:** TypeScript  |  **Stars:** 9,509  |  **Forks:** 1,227  |  **Score:** 3,467  |  **Created:** 2025-10-16

**Background:** Pascal Editor is a 3D building editor built with React Three Fiber and WebGPU, structured as a Turborepo monorepo separating core logic (schemas, state management, spatial queries) from the 3D viewer and editor UI. With 9,500 stars, it demonstrates the maturing capability of browser-based architectural design using modern web GPU standards.

**Problem it solves:** 3D building design traditionally requires heavy desktop applications like SketchUp or Blender. Pascal Editor brings architectural modeling to the browser with WebGPU acceleration, eliminating installation requirements and enabling collaborative web-based workflows for creating and sharing projects.

**Why another one?** The WebGPU foundation is the key differentiator. While WebGL-based 3D editors exist, Pascal Editor leverages WebGPU's compute shaders and modern rendering pipeline for significantly better performance. The clean three-package separation (core, viewer, editor) makes it highly extensible for domain-specific building tools.

---

## 12. [ruflo](https://github.com/ruvnet/ruflo)
> The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems.

**Language:** TypeScript  |  **Stars:** 30,011  |  **Forks:** 3,321  |  **Score:** 3,366  |  **Created:** 2025-06-02

**Background:** RuFlo v3.5 is an enterprise AI orchestration platform for deploying multi-agent swarms, coordinating autonomous workflows, and building conversational AI systems. With 30,000 stars and native Claude Code and Codex integration, it provides enterprise-grade architecture with distributed swarm intelligence and RAG integration.

**Problem it solves:** Deploying multiple AI agents in production requires coordination, state management, and fault tolerance that individual agent tools do not provide. RuFlo handles distributed swarm orchestration, agent lifecycle management, and workflow coordination at enterprise scale.

**Why another one?** RuFlo's enterprise-grade positioning — distributed swarm intelligence, production deployment tooling, and native Claude Code integration — targets organizations moving beyond single-agent prototypes. The v3.5 release demonstrates sustained development, and the 30,000-star count signals real production adoption.

---

## 13. [strix](https://github.com/usestrix/strix)
> Open-source AI hackers to find and fix your app's vulnerabilities.

**Language:** Python  |  **Stars:** 23,159  |  **Forks:** 2,499  |  **Score:** 3,072  |  **Created:** 2025-08-05

**Background:** Strix is an open-source AI security platform that deploys autonomous AI "hackers" to find and fix vulnerabilities in web applications. With over 23,000 stars since its August 2025 launch, it has established itself as a leading open-source alternative to commercial application security testing tools.

**Problem it solves:** Application security testing is expensive and often performed too infrequently — typically only before major releases. Strix enables continuous, automated vulnerability discovery by deploying AI agents that think like attackers, identifying security flaws before real hackers do.

**Why another one?** Strix's dual focus on finding and fixing vulnerabilities sets it apart from tools that only report issues. The AI-driven approach adapts to each application's unique attack surface rather than running generic scan patterns, and the open-source model enables community-contributed attack strategies.

---

## 14. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 109,016  |  **Forks:** 18,014  |  **Score:** 3,060  |  **Created:** 2025-02-22

**Background:** Claude Code by Anthropic is the official agentic coding tool that operates from the terminal, understanding codebases and executing tasks through natural language. Surpassing 109,000 stars, it has become the platform that much of today's trending list is built upon — skills, agents, and workflows designed specifically for Claude Code dominate the chart.

**Problem it solves:** Developers spend significant time on routine coding tasks, context-switching between documentation, code, and terminal. Claude Code brings AI assistance directly into the terminal workflow, handling everything from code generation to git operations to complex debugging without leaving the developer's primary environment.

**Why another one?** As the official Anthropic product, Claude Code benefits from direct integration with Claude's capabilities and first-party support. Its terminal-native design appeals to developers who prefer CLI over IDE-based AI tools, and the thriving ecosystem of skills and plugins (visible across this trending list) creates a self-reinforcing adoption cycle.

---

## 15. [TorchCode](https://github.com/duoan/TorchCode)
> LeetCode for PyTorch — practice implementing softmax, attention, GPT-2 and more from scratch with instant auto-grading. Jupyter-based, self-hosted or try online.

**Language:** Jupyter Notebook  |  **Stars:** 3,389  |  **Forks:** 278  |  **Score:** 3,040  |  **Created:** 2026-03-04

**Background:** TorchCode is a practice platform for PyTorch implementation skills, structured like LeetCode but focused on tensor operations and neural network architectures. Released three weeks ago, it offers Jupyter-based exercises where users implement operators like softmax, attention mechanisms, and GPT-2 from scratch with instant auto-grading.

**Problem it solves:** ML engineering interviews increasingly test candidates' ability to implement core operations from scratch, but no structured practice platform existed for this skill. TorchCode fills the gap with progressive exercises that build from basic tensor operations to full architecture implementations.

**Why another one?** The "LeetCode for PyTorch" positioning is perfectly targeted at the ML job market. Unlike general ML courses that focus on theory, TorchCode emphasizes hands-on implementation with immediate feedback. The self-hosted Jupyter design means users can practice on their own hardware with their own GPU, and the online option lowers the barrier to entry.

---

## 16. [carbonyl](https://github.com/fathyb/carbonyl)
> Chromium running inside your terminal

**Language:** Rust  |  **Stars:** 18,091  |  **Forks:** 467  |  **Score:** 2,900  |  **Created:** 2023-01-20

**Background:** Carbonyl is a Chromium-based browser that renders web pages directly in the terminal using ANSI escape sequences. Originally released in January 2023, it has accumulated over 18,000 stars and continues to trend as terminal-based workflows gain popularity with the rise of agentic coding tools.

**Problem it solves:** Developers working primarily in the terminal need to switch to a graphical browser for any web-related task. Carbonyl eliminates this context switch by rendering full web pages — including JavaScript, CSS, and images — directly in the terminal.

**Why another one?** Carbonyl renders actual Chromium rather than simplified HTML, meaning it handles modern JavaScript-heavy websites that terminal browsers like Lynx or w3m cannot. The Rust implementation provides the performance needed for real-time rendering, and its resurgence in trending lists suggests renewed relevance in the agent-driven, terminal-first development era.

---

## 17. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 71,854  |  **Forks:** 11,138  |  **Score:** 2,874  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski provides a collection of pre-built AI agent personas for professional roles. Now at nearly 72,000 stars (up from 61,000 just three days ago), it continues its remarkable growth. Each agent has defined personality traits, processes, and deliverable templates covering roles from frontend development to community management.

**Problem it solves:** Teams adopting AI agents need role-specific system prompts and workflow definitions for every business function. Agency Agents provides these ready-made, eliminating the prompt engineering overhead of creating effective personas from scratch.

**Why another one?** The personality-driven approach — agents with names, quirks, and strong opinions — makes them entertaining and shareable, driving viral adoption beyond the typical developer audience. The breadth of covered roles positions it as an agency-in-a-box rather than just a prompt library, and the 72,000-star growth trajectory validates the concept.

---

## 18. [chandra](https://github.com/datalab-to/chandra)
> OCR model that handles complex tables, forms, handwriting with full layout.

**Language:** Python  |  **Stars:** 8,339  |  **Forks:** 851  |  **Score:** 2,854  |  **Created:** 2025-10-08

**Background:** Chandra is an OCR model from Datalab that handles complex document layouts including tables, forms, and handwriting with full layout preservation. Part of the broader Datalab document intelligence suite, it provides state-of-the-art extraction accuracy for the most challenging document types that traditional OCR tools struggle with.

**Problem it solves:** Standard OCR tools fail on complex document layouts — multi-column tables, nested forms, and handwritten annotations are typically mangled or lost entirely. Chandra preserves the full spatial layout of documents, correctly associating labels with values in forms and maintaining table structure.

**Why another one?** Chandra's focus on layout-aware OCR for the hardest document types (tables, forms, handwriting) targets the cases where general-purpose OCR falls short. The integration with Datalab's broader document intelligence platform provides a complete pipeline from raw document to structured data.

---

## 19. [HolyClaude](https://github.com/CoderLuii/HolyClaude)
> AI coding workstation: Claude Code + web UI + 7 AI CLIs + headless browser + 50+ tools

**Language:** Dockerfile  |  **Stars:** 1,856  |  **Forks:** 207  |  **Score:** 2,852  |  **Created:** 2026-03-22

**Background:** HolyClaude is a containerized AI coding workstation that bundles Claude Code with a web UI, seven AI CLIs, a headless browser, and over 50 development tools into a single Docker image. Released just four days ago, it has quickly gathered 1,856 stars, available in eleven languages, indicating broad international appeal.

**Problem it solves:** Setting up a complete AI-augmented development environment requires installing and configuring dozens of tools individually — Claude Code, browser automation, multiple AI CLIs, and supporting utilities. HolyClaude packages everything into a single Docker container that is ready to use immediately.

**Why another one?** The Docker-first approach makes HolyClaude instantly reproducible and portable — spin up a full AI workstation on any machine with a single command. The inclusion of seven AI CLIs alongside Claude Code makes it tool-agnostic, and the headless browser enables web automation workflows without additional setup.

---

## 20. [bb-browser](https://github.com/epiral/bb-browser)
> Your browser is the API. CLI + MCP server for AI agents to control Chrome with your login state.

**Language:** TypeScript  |  **Stars:** 4,114  |  **Forks:** 395  |  **Score:** 2,792  |  **Created:** 2026-01-31

**Background:** BB-Browser (BadBoy Browser) provides a CLI and MCP server that lets AI agents control Chrome using the user's existing login state. Rather than requiring API keys or building scrapers, it leverages the fact that users are already logged into Twitter, Reddit, YouTube, GitHub, and other services in their browser.

**Problem it solves:** AI agents that need to interact with authenticated web services face a painful choice: manage separate API credentials (when available) or build fragile authentication flows. BB-Browser eliminates this by reusing the user's existing Chrome sessions — no keys, no bots, no scrapers.

**Why another one?** The "your browser is the API" philosophy is the differentiator. While tools like Playwright and Puppeteer require building authentication flows for each service, BB-Browser treats the user's authenticated Chrome as a ready-made API. The MCP server integration means any MCP-compatible AI agent can control the browser natively.

---

## 21. [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
> Teams-first Multi-agent orchestration for Claude Code

**Language:** TypeScript  |  **Stars:** 24,305  |  **Forks:** 2,215  |  **Score:** 2,728  |  **Created:** 2026-01-09

**Background:** Oh-My-ClaudeCode by Yeachan Heo is a teams-first multi-agent orchestration framework for Claude Code. Available in seven languages and with 24,000 stars in under three months, it provides a structured approach to coordinating multiple Claude Code agents working on the same codebase.

**Problem it solves:** Running multiple Claude Code agents on a shared codebase leads to conflicts, duplicated work, and inconsistent code. Oh-My-ClaudeCode provides orchestration that coordinates agent activities, prevents conflicts, and ensures agents work as a cohesive team rather than independent actors.

**Why another one?** The "teams-first" design philosophy means orchestration is not bolted on — it is the core architecture. While other multi-agent frameworks treat coordination as a feature, Oh-My-ClaudeCode builds every capability around the assumption that multiple agents must collaborate safely and efficiently on shared resources.

---

## 22. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**Language:** TypeScript  |  **Stars:** 64,509  |  **Forks:** 8,786  |  **Score:** 2,660  |  **Created:** 2026-03-11

**Background:** Gstack by Garry Tan (Y Combinator CEO) packages 23 opinionated workflow skills for Claude Code as slash commands. In just fifteen days since release, it has amassed 64,500 stars — driven by Tan's high profile and the project's practical utility. Each skill maps to a specialist role in a software team.

**Problem it solves:** A single Claude Code session treats every request uniformly, with no role-specific depth. Gstack partitions workflows into specialist modes: CEO review rethinks the product vision, eng review locks in architecture, design review evaluates UI decisions, and ship handles the entire release process.

**Why another one?** The celebrity factor of Y Combinator's CEO sharing his personal setup drives initial adoption, but the substance is in the opinionated defaults. Gstack's growth from 40,000 to 64,500 stars in three days demonstrates that the value extends well beyond name recognition — developers are finding real productivity gains from the specialist role partitioning.

---

## 23. [app-ideas](https://github.com/florinpop17/app-ideas)
> A Collection of application ideas which can be used to improve your coding skills.

**Language:** N/A  |  **Stars:** 92,469  |  **Forks:** 10,361  |  **Score:** 2,634  |  **Created:** 2019-02-25

**Background:** App Ideas is a community-curated collection of application project ideas organized by difficulty level, now with over 92,000 stars after seven years of continuous contributions. It provides structured project specifications for developers looking to practice or experiment with new technologies.

**Problem it solves:** Developers wanting to practice or learn new technologies often struggle with "what to build." App Ideas provides a curated directory of project specifications with clear requirements, organized from beginner to advanced, eliminating the ideation barrier to practice.

**Why another one?** As a seven-year-old repository with 92,000 stars, app-ideas is the definitive project ideas collection. Its continued trending suggests renewed relevance in the AI era — developers may be using these structured project specifications as prompts for AI coding agents, giving them well-defined tasks to practice and evaluate agent capabilities.

---

## 24. [skills](https://github.com/MiniMax-AI/skills)
> Development skills for AI coding agents. Plug into your favorite AI coding tool and get structured, production-quality guidance for frontend, fullstack, Android, iOS, and shader development.

**Language:** C#  |  **Stars:** 9,279  |  **Forks:** 748  |  **Score:** 2,619  |  **Created:** 2026-03-17

**Background:** MiniMax Skills is a collection of development skills for AI coding agents, released nine days ago by MiniMax AI. Still in beta, it provides structured guidance for frontend, fullstack, Android, iOS, and shader development that can be plugged into any AI coding tool. Its growth from 3,670 to 9,279 stars in three days reflects strong demand for domain-specific agent skills.

**Problem it solves:** AI coding agents produce inconsistent results across different development domains because they lack domain-specific best practices. MiniMax Skills provides curated, production-quality guidance for each platform — ensuring agents follow established patterns for animations, state management, responsive layouts, and platform-specific conventions.

**Why another one?** MiniMax Skills covers an unusually broad platform matrix — frontend, fullstack, Android, iOS, and shaders — in a single package. Most competing skill sets focus on a single domain. The plugin-agnostic design means these skills work with Claude Code, Cursor, Copilot, and other tools without modification.

---

## 25. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 66,296  |  **Forks:** 9,496  |  **Score:** 2,458  |  **Created:** 2026-03-06

**Background:** Autoresearch by Andrej Karpathy gives an AI agent a small but real LLM training setup and lets it experiment autonomously overnight. Now at 66,000 stars (up from 51,000 three days ago), the project's evocative README — imagining a future where research is "entirely the domain of autonomous swarms of AI agents" — continues to capture the community's imagination.

**Problem it solves:** AI research experimentation is bottlenecked by human availability — researchers can only run and analyze so many experiments per day. Autoresearch automates the experiment cycle: the agent formulates hypotheses, modifies training code, runs experiments on a single GPU, analyzes results, and iterates.

**Why another one?** Karpathy's name carries enormous weight in the AI community, but the substance is in the simplicity. Rather than building a complex research orchestration platform, autoresearch demonstrates that a single agent with a single GPU can make meaningful research progress overnight — a proof of concept with implications for how AI research labs allocate resources.

---

> **Day's theme:** The agent ecosystem enters its infrastructure phase — from memory engines and LLM gateways to browser APIs and OCR pipelines — as the community builds the foundational services that specialized agent skills and multi-agent orchestration platforms depend on, while established projects like Superpowers, DeerFlow, and Gstack continue their explosive star growth.
