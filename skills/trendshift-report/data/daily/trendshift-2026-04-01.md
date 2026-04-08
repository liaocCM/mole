# Trendshift Report — 2026-04-01
**Total:** 25 repositories

---

## 1. [claw-code](https://github.com/instructkr/claw-code)
> Better Harness Tools, not merely storing the archive of leaked Claude Code but also make real things done. Now rewriting in Rust.

**Language:** Rust  |  **Stars:** 48,386  |  **Forks:** 56,314  |  **Score:** 350,303  |  **Created:** 2026-03-31

**Background:** Claw Code by InstructKR (originally from ultraworkers) is a Rust rewrite of a Claude Code-inspired agent harness. Created just yesterday, it has already exploded to 48,000 stars with an unusual fork-to-star ratio exceeding 1:1, suggesting widespread forking for customization or deployment rather than passive interest.

**Problem it solves:** Developers who want an open, self-hostable alternative to proprietary agent harnesses need a performant, extensible foundation. Claw Code provides a Rust-based workspace with parity tracking against the original tooling, offering better performance and memory safety for production agent deployments.

**Why another one?** The Rust rewrite is the key differentiator — moving from a scripting language to Rust provides the performance and reliability needed for always-on agent harnesses. The project's rapid adoption and active parity tracking suggest it fills a genuine gap for teams wanting full control over their agent infrastructure.

---

## 2. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 110,318  |  **Forks:** 18,343  |  **Score:** 57,812  |  **Created:** 2025-02-22

**Background:** Claude Code by Anthropic is the official agentic coding tool that operates directly in the terminal, IDE, or via GitHub mentions. Surpassing 110,000 stars, it has become the most widely adopted terminal-based AI coding agent, with installation now recommended via standalone methods rather than npm.

**Problem it solves:** Developers spend significant time on routine coding tasks — file navigation, git workflows, code explanations, and boilerplate generation. Claude Code handles these through natural language commands while maintaining full codebase context, eliminating the friction of switching between coding and AI interfaces.

**Why another one?** As the first-party tool from Anthropic, Claude Code has direct access to the latest Claude models and receives immediate feature updates. Its terminal-native design and GitHub integration provide a seamless workflow that browser-based alternatives cannot match.

---

## 3. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 32,742  |  **Forks:** 3,011  |  **Score:** 20,534  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice by shanraisshan is a community-maintained guide documenting proven patterns, tips, and implementation strategies for Claude Code. Updated as recently as April 6, 2026 for Claude Code v2.1.92, it has grown to over 32,000 stars as the definitive practitioner reference for the ecosystem.

**Problem it solves:** Claude Code's capabilities expand rapidly with each release, but effective usage patterns are discovered through trial and error. This repository consolidates community-learned best practices, orchestration workflows, and implementation patterns into a continuously updated reference.

**Why another one?** Unlike official documentation that focuses on features, this captures the practitioner perspective — what works in daily use, common pitfalls, and workflow patterns from real-world usage. The community-driven nature ensures it reflects diverse use cases and stays current with each release.

---

## 4. [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
> OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more.

**Language:** TypeScript  |  **Stars:** 18,118  |  **Forks:** 1,711  |  **Score:** 15,774  |  **Created:** 2026-02-02

**Background:** Oh My Codex (OMX) by Yeachan Heo is an enhancement layer for OpenAI's Codex CLI that adds hooks, agent teams, HUDs, and extended capabilities. With over 18,000 stars in two months, it has established itself as the primary customization framework for Codex users who want more structured workflows.

**Problem it solves:** Codex CLI out of the box provides a capable but bare coding agent. OMX layers on better prompts, workflow orchestration, and runtime helpers that make the agent more effective as projects grow in complexity — turning a solo agent into a coordinated team.

**Why another one?** OMX is specifically designed for the Codex ecosystem rather than being a generic agent framework. Its npm-installable approach and focus on progressive enhancement — start simple, add capabilities as needed — makes it accessible without requiring a complete workflow overhaul.

---

## 5. [pretext](https://github.com/chenglou/pretext)
> Fast, accurate & comprehensive text measurement & layout

**Language:** TypeScript  |  **Stars:** 39,924  |  **Forks:** 2,122  |  **Score:** 14,332  |  **Created:** 2026-03-07

**Background:** Pretext by chenglou is a pure JavaScript/TypeScript library for multiline text measurement and layout that sidesteps DOM measurements entirely. In under a month since release, it has amassed nearly 40,000 stars — a remarkable trajectory for a low-level text rendering library, reflecting deep demand for performant text handling in the web ecosystem.

**Problem it solves:** DOM-based text measurement via `getBoundingClientRect` and `offsetHeight` triggers layout reflow — one of the most expensive browser operations. Pretext implements its own text measurement logic using the browser's font engine as ground truth, eliminating reflow-triggered performance bottlenecks.

**Why another one?** Pretext's approach of reimplementing text measurement outside the DOM is architecturally novel. It supports rendering to DOM, Canvas, SVG, and soon server-side, making it uniquely versatile. The AI-friendly iteration method for calibrating against native font engines ensures accuracy without the performance cost.

---

## 6. [VibeVoice](https://github.com/microsoft/VibeVoice)
> Open-Source Frontier Voice AI

**Language:** Python  |  **Stars:** 37,119  |  **Forks:** 4,268  |  **Score:** 12,344  |  **Created:** 2025-08-25

**Background:** VibeVoice by Microsoft is an open-source frontier voice AI platform covering text-to-speech, ASR, and audio processing. With published papers on both TTS and ASR, a Hugging Face model collection, and Colab demos, it represents Microsoft's bid to democratize production-quality voice AI with over 37,000 stars.

**Problem it solves:** Building production-grade voice AI requires assembling multiple models for speech synthesis, recognition, and processing. VibeVoice provides a unified, open-source platform with streaming TTS, ASR, and an interactive playground — reducing the integration burden from months to minutes.

**Why another one?** Microsoft's institutional backing provides the research depth (published papers) and engineering quality that most open-source voice projects lack. The streaming TTS capability and comprehensive model collection on Hugging Face make it production-ready out of the box, unlike research-only alternatives.

---

## 7. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 138,686  |  **Forks:** 11,746  |  **Score:** 10,683  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, now at 138,000 stars. It enforces a disciplined spec-plan-implement-review process where the agent teases out requirements, presents them in digestible chunks, builds an implementation plan, then launches subagent-driven development with built-in review cycles.

**Problem it solves:** Coding agents left unconstrained jump straight into writing code without understanding the full problem. Superpowers enforces a structured methodology — spec, plan, implement, review — ensuring agents work methodically through TDD and YAGNI principles rather than producing poorly planned implementations.

**Why another one?** Superpowers focuses on development methodology rather than tool orchestration. Its subagent-driven model allows agents to work autonomously for hours without drifting from the plan. At 138,000 stars, it has proven its approach at scale and continues to grow as the reference implementation for structured agent development.

---

## 8. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**Language:** JavaScript  |  **Stars:** 144,531  |  **Forks:** 22,174  |  **Score:** 9,901  |  **Created:** 2026-01-18

**Background:** Everything Claude Code by Affaan M is a comprehensive performance optimization system for AI coding agents, now the most-starred project in the agent harness category at 144,000 stars. Available in seven languages, it provides skills, instincts, memory management, security guardrails, and research-first development patterns across Claude Code, Codex, Opencode, and Cursor.

**Problem it solves:** AI coding agents out of the box lack optimized workflows for different development scenarios. Everything Claude Code provides a curated system of skills and instincts that make agents more effective — better at planning, more security-conscious, and more consistent in output quality.

**Why another one?** The cross-platform support (Claude Code, Codex, Opencode, Cursor) makes it uniquely portable. At 144,000 stars, network effects drive continuous community contributions and validation, creating a feedback loop that keeps it ahead of single-platform alternatives.

---

## 9. [openscreen](https://github.com/siddharthvaddem/openscreen)
> Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio.

**Language:** TypeScript  |  **Stars:** 24,842  |  **Forks:** 1,650  |  **Score:** 8,844  |  **Created:** 2025-10-10

**Background:** OpenScreen by Siddharth Vaddem is a free, open-source alternative to Screen Studio for creating polished demo recordings. Still in beta, it has attracted nearly 25,000 stars by offering the core screen recording and beautification features without the $29/month subscription or watermarks.

**Problem it solves:** Creating professional-looking product demos typically requires expensive tools like Screen Studio. OpenScreen provides the essential features — screen recording with beautification — for free, with no watermarks and commercial-use licensing.

**Why another one?** The zero-cost, no-watermark, commercial-use-friendly licensing is the primary draw. While it self-describes as a simpler version of Screen Studio, the open-source model means the community can extend it beyond what any single commercial vendor would prioritize.

---

## 10. [claude-howto](https://github.com/luongnv89/claude-howto)
> A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

**Language:** Python  |  **Stars:** 20,611  |  **Forks:** 2,462  |  **Score:** 7,988  |  **Created:** 2025-11-07

**Background:** Claude How To by luongnv89 is a visual, example-driven guide to Claude Code that previously reached number-one on GitHub trending. With over 20,000 stars, it bridges the gap between official documentation and practical application through copy-paste templates and progressive examples from basic concepts to advanced agent workflows.

**Problem it solves:** Official documentation explains what Claude Code can do but not how to apply it to real workflows. Claude How To provides concrete, copy-paste-ready templates that deliver immediate value — eliminating the gap between reading about features and actually using them productively.

**Why another one?** The visual, example-driven approach differentiates it from text-heavy documentation and best-practice guides. Its progressive structure — from basics to advanced agents — serves both newcomers and experienced users, and the template-first design ensures every section delivers actionable content.

---

## 11. [vphone-aio](https://github.com/34306/vphone-aio)
> 1 script run the vphone

**Language:** Shell  |  **Stars:** 3,052  |  **Forks:** 550  |  **Score:** 6,750  |  **Created:** 2026-02-28

**Background:** vphone-aio by 34306 is a single-script solution for running a virtual phone (iOS 26.1) on macOS, pre-jailbroken with full bootstrap installed. The 12GB package includes everything needed to boot a virtualized iOS environment, requiring only SIP disabled and AMFI bypassed on the host machine.

**Problem it solves:** Running iOS environments for testing, development, or research typically requires physical Apple hardware or complex virtualization setups. vphone-aio reduces this to a single script that downloads and configures everything automatically, lowering the barrier to iOS experimentation.

**Why another one?** The all-in-one approach — a single script that handles download, extraction, and configuration — eliminates the multi-step setup that plagues other iOS virtualization methods. The pre-jailbroken state with full bootstrap means developers can immediately access the file system and install tools without additional steps.

---

## 12. [sherlock](https://github.com/sherlock-project/sherlock)
> Hunt down social media accounts by username across social networks

**Language:** Python  |  **Stars:** 80,033  |  **Forks:** 9,304  |  **Score:** 6,634  |  **Created:** 2018-12-24

**Background:** Sherlock is a long-standing OSINT tool that searches for usernames across social networks simultaneously. With 80,000 stars and over seven years of active development, it remains the most popular open-source username enumeration tool, periodically resurfacing on trending lists as new users discover it.

**Problem it solves:** Investigating whether a username exists across hundreds of social platforms is tedious when done manually. Sherlock automates this by querying hundreds of sites in parallel, producing a comprehensive report of where a given username is registered.

**Why another one?** Sherlock's longevity and community size are unmatched — seven years of site coverage updates mean it supports more platforms than any alternative. Its Python simplicity and CLI interface make it accessible to both security professionals and casual users.

---

## 13. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> List of Computer Science courses with video lectures.

**Language:** N/A  |  **Stars:** 79,585  |  **Forks:** 10,945  |  **Score:** 6,140  |  **Created:** 2016-10-21

**Background:** CS Video Courses by Developer-Y is a curated list of university-level computer science courses with video lectures, maintained since 2016. With nearly 80,000 stars, it is one of the most popular educational resources on GitHub, providing structured pathways through CS fundamentals via actual college course recordings.

**Problem it solves:** Finding quality, university-level CS education online requires sifting through MOOCs, tutorials, and promotional content. This repository curates only genuine college and university courses with video lectures, providing a trusted directory of rigorous educational content.

**Why another one?** The strict curation policy — only actual college/university-level courses, no MOOCs or tutorials — ensures consistently high quality. A decade of community maintenance has built a comprehensive directory that no single platform can match in breadth of academic coverage.

---

## 14. [coding-interview-university](https://github.com/jwasham/coding-interview-university)
> A complete computer science study plan to become a software engineer.

**Language:** N/A  |  **Stars:** 340,398  |  **Forks:** 81,887  |  **Score:** 6,098  |  **Created:** 2016-06-06

**Background:** Coding Interview University by John Washam is one of GitHub's most-starred repositories at 340,000 stars — a comprehensive self-study plan that the author used to land a job at Amazon. It covers everything from data structures and algorithms to system design and behavioral interviews.

**Problem it solves:** Preparing for software engineering interviews at top companies requires a structured study plan covering CS fundamentals, algorithms, system design, and more. Coding Interview University provides a complete, battle-tested curriculum that takes the guesswork out of interview preparation.

**Why another one?** The author's personal success story (hired at Amazon after following this plan) provides credible validation. At 340,000 stars, it benefits from continuous community refinement and has become the de facto standard for self-directed interview preparation.

---

## 15. [codex](https://github.com/openai/codex)
> Lightweight coding agent that runs in your terminal

**Language:** Rust  |  **Stars:** 73,603  |  **Forks:** 10,352  |  **Score:** 5,653  |  **Created:** 2025-04-13

**Background:** Codex CLI by OpenAI is a lightweight terminal-based coding agent, now also available as a desktop app and IDE extension for VS Code, Cursor, and Windsurf. With 73,000 stars and a Rust implementation, it competes directly with Claude Code in the terminal-based agent space while also offering a cloud-based web version.

**Problem it solves:** Developers need AI coding assistance that integrates into their existing terminal workflow without requiring browser context-switching. Codex CLI provides local execution with natural language commands, handling code generation, refactoring, and explanation directly in the terminal.

**Why another one?** OpenAI's brand and model ecosystem give Codex CLI a built-in user base. The multi-surface strategy — CLI, desktop app, IDE extension, and web — provides more flexibility than terminal-only alternatives. The Rust implementation ensures minimal resource overhead on developer machines.

---

## 16. [sentrysearch](https://github.com/ssrajadh/sentrysearch)
> Semantic search over videos using Gemini Embedding 2 or Qwen3-VL.

**Language:** Python  |  **Stars:** 3,006  |  **Forks:** 293  |  **Score:** 4,858  |  **Created:** 2026-03-17

**Background:** SentrySearch by ssrajadh enables semantic search over video footage — type what you are looking for and get a trimmed clip back. It splits videos into overlapping chunks, embeds each chunk using Gemini Embedding 2 or a local Qwen3-VL model, and stores vectors in ChromaDB for retrieval.

**Problem it solves:** Finding specific moments in video footage requires scrubbing through hours of content manually. SentrySearch allows natural language queries against video archives, automatically returning trimmed clips matching the search — turning passive footage into a searchable database.

**Why another one?** The dual embedding approach (cloud Gemini or local Qwen3-VL) provides flexibility between convenience and privacy. The automatic clip trimming sets it apart from tools that merely return timestamps — users get a ready-to-use video clip rather than a pointer to manually extract.

---

## 17. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
> Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**Language:** Python  |  **Stars:** 74,982  |  **Forks:** 10,187  |  **Score:** 4,682  |  **Created:** 2020-05-08

**Background:** PaddleOCR by Baidu's PaddlePaddle team is a global-leading OCR toolkit and document AI engine supporting 100+ languages. With nearly 75,000 stars and six years of development, it has evolved from a pure OCR library into a comprehensive document processing platform that bridges the gap between images/PDFs and LLMs.

**Problem it solves:** Extracting structured text from images, scanned documents, and PDFs remains a fundamental bottleneck in document processing workflows. PaddleOCR provides production-grade OCR with multi-language support, used by over 6,000 downstream repositories as the extraction layer feeding data into AI pipelines.

**Why another one?** PaddleOCR's 100+ language support and lightweight architecture make it uniquely suitable for global deployments. Its positioning as a bridge between documents and LLMs reflects the current demand for structured data extraction as a prerequisite for AI-powered document understanding.

---

## 18. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 74,280  |  **Forks:** 11,645  |  **Score:** 4,223  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski provides a collection of pre-built AI agent personas for professional roles. Now at over 74,000 stars (up significantly from recent weeks), it continues explosive growth. Each agent has defined personality traits, processes, and deliverable templates covering roles from frontend development to community management.

**Problem it solves:** Teams adopting AI agents need role-specific system prompts and workflow definitions for every business function. Agency Agents provides these ready-made, eliminating the prompt engineering overhead of creating effective personas from scratch.

**Why another one?** The personality-driven approach — agents with names, quirks, and strong opinions — makes them entertaining and shareable, driving viral adoption beyond the typical developer audience. The breadth of covered roles positions it as an agency-in-a-box rather than just a prompt library.

---

## 19. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 26,562  |  **Forks:** 3,478  |  **Score:** 4,110  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is an adaptive AI agent platform built on the Hermes model family, with comprehensive documentation, Discord community, and MIT licensing. At over 26,000 stars, it represents the open-source AI research community's approach to building agents that learn and improve through usage.

**Problem it solves:** Most AI agents are static — they perform the same way regardless of how much they are used. Hermes Agent is designed to grow with its user, adapting its capabilities and knowledge over time to become increasingly effective at the specific tasks and domains its operator cares about.

**Why another one?** Nous Research's expertise in fine-tuning and model training gives Hermes Agent a unique advantage in the adaptation mechanism. The "grows with you" philosophy differentiates it from agents that rely solely on prompt engineering, offering genuine capability improvement over time.

---

## 20. [pm-skills](https://github.com/phuryn/pm-skills)
> PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth.

**Language:** N/A  |  **Stars:** 9,652  |  **Forks:** 1,040  |  **Score:** 4,108  |  **Created:** 2026-03-01

**Background:** PM Skills Marketplace by phuryn is a collection of 65 PM skills and 36 chained workflows across 8 plugins, designed for Claude Code and Cowork. In just one month since release, it has gathered nearly 10,000 stars by providing structured product management workflows — from discovery through strategy, execution, launch, and growth.

**Problem it solves:** Product managers spend hours on repetitive analytical and documentation tasks — competitive analysis, PRD writing, launch planning, and growth strategy. PM Skills automates these through chained workflows where one skill's output feeds the next, creating end-to-end product management pipelines.

**Why another one?** PM Skills targets product managers specifically rather than developers, filling a gap in the agent skills ecosystem. The chained workflow design — where `/discover` flows into `/strategy` flows into `/execute` — mirrors actual PM workflows rather than providing isolated tools.

---

## 21. [ink](https://github.com/vadimdemedes/ink)
> React for interactive command-line apps

**Language:** TypeScript  |  **Stars:** 37,290  |  **Forks:** 940  |  **Score:** 3,334  |  **Created:** 2017-06-12

**Background:** Ink by Vadim Demedes brings React's component model to command-line interfaces, allowing developers to build interactive terminal apps using familiar JSX syntax. At 37,000 stars and nine years of development, it is the established standard for React-based CLI applications and likely trending due to renewed interest from the agent UI ecosystem.

**Problem it solves:** Building interactive terminal UIs traditionally requires imperative cursor manipulation and escape codes. Ink provides React's declarative component model — state management, hooks, flexbox layout — for the terminal, making complex CLI interfaces as composable as web interfaces.

**Why another one?** Ink's React foundation means any developer familiar with React can immediately build terminal UIs without learning new paradigms. The nine years of maturity, extensive component ecosystem, and near-universal adoption in modern CLI tools make it the de facto standard.

---

## 22. [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)
> freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**Language:** TypeScript  |  **Stars:** 441,907  |  **Forks:** 44,140  |  **Score:** 3,252  |  **Created:** 2014-12-24

**Background:** freeCodeCamp is GitHub's most-starred repository and the world's largest open-source learning platform. Its curriculum covers math, programming, and computer science through interactive coding challenges, with millions of learners worldwide. It perennially trends as new cohorts discover it.

**Problem it solves:** Quality programming education remains expensive and inaccessible to many. freeCodeCamp provides a complete, interactive curriculum — from HTML basics through machine learning — entirely free, with certifications that validate learning without financial barriers.

**Why another one?** At 441,000 stars and over a decade of development, freeCodeCamp has no peer in scale or community size. Its open-source model means the curriculum is continuously improved by thousands of contributors, and its non-profit structure ensures it remains free permanently.

---

## 23. [timesfm](https://github.com/google-research/timesfm)
> TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting.

**Language:** Python  |  **Stars:** 15,252  |  **Forks:** 1,336  |  **Score:** 3,249  |  **Created:** 2024-04-29

**Background:** TimesFM by Google Research is a pretrained foundation model for time-series forecasting, published at ICML 2024. Now at version 2.5 with checkpoints on Hugging Face and integration into BigQuery as an official Google product, it represents the foundation model paradigm applied to temporal data with over 15,000 stars.

**Problem it solves:** Traditional time-series forecasting requires domain-specific model selection and extensive feature engineering for each dataset. TimesFM provides a single pretrained model that generalizes across domains — financial, weather, IoT, healthcare — without per-dataset training.

**Why another one?** Google Research's publication at ICML 2024 provides academic rigor, and the BigQuery integration makes it the only time-series foundation model available as a managed Google Cloud product. The progression from research artifact to production service (version 2.5) demonstrates sustained investment.

---

## 24. [flash-moe](https://github.com/danveloper/flash-moe)
> Running a big model on a small laptop

**Language:** Objective-C  |  **Stars:** 3,342  |  **Forks:** 391  |  **Score:** 3,239  |  **Created:** 2026-03-18

**Background:** Flash MoE by danveloper enables running large mixture-of-experts models on consumer laptops, likely leveraging Apple Silicon's unified memory architecture given the Objective-C implementation. With 3,300 stars in two weeks, it addresses the growing demand for local model inference on personal hardware.

**Problem it solves:** Large MoE models like Mixtral or DeepSeek typically require server-grade GPUs with substantial VRAM. Flash MoE optimizes inference to run these models on laptops, bringing frontier-class model capabilities to personal devices without cloud dependencies.

**Why another one?** The Objective-C implementation suggests deep integration with Apple's Metal framework and unified memory, potentially extracting more performance from MacBooks than generic GGML-based solutions. Running "big models on small laptops" captures the zeitgeist of local-first AI.

---

## 25. [phantom](https://github.com/ghostwright/phantom)
> An AI co-worker with its own computer. Self-evolving, persistent memory, MCP server, secure credential collection, email identity. Built on the Claude Agent SDK.

**Language:** TypeScript  |  **Stars:** 1,216  |  **Forks:** 145  |  **Score:** 3,075  |  **Created:** 2026-03-26

**Background:** Phantom by Ghostwright is an AI co-worker built on the Claude Agent SDK that operates with its own computer environment. Released just six days ago with 822 passing tests and Docker support, it provides self-evolving capabilities, persistent memory, an MCP server, secure credential management, and email identity — essentially giving an AI agent a full digital presence.

**Problem it solves:** AI agents typically operate as ephemeral tools that lose context between sessions and lack persistent identity. Phantom provides an agent with its own computer, memory, credentials, and email — enabling it to function as an ongoing co-worker rather than a one-shot assistant.

**Why another one?** The "own computer" model is the key differentiator. Rather than running inside a user's environment, Phantom operates in an isolated Docker container with its own identity, making it suitable for autonomous background work. Built on the Claude Agent SDK, it leverages Anthropic's official agent infrastructure rather than custom orchestration.

---

> **Day's theme:** The Claude Code and agent harness ecosystem dominates the trending chart with 15 of 25 repos directly related to agentic coding tools — from the explosive overnight rise of Claw Code's Rust rewrite to established giants like Superpowers and Everything Claude Code — while the remaining slots split between perennial educational resources, specialized AI applications in voice, video search, and time-series forecasting, and infrastructure tools that give agents their own computers, text rendering engines, and local model inference capabilities.
