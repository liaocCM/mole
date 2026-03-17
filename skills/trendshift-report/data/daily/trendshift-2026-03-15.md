# Trendshift Report — 2026-03-15
**Total:** 25 repositories

---

## 1. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 10 opinionated tools that serve as CEO, Eng Manager, Release Manager, Doc Engineer, and QA

**Language:** TypeScript  |  **Stars:** 17,806  |  **Forks:** 1,980  |  **Score:** 22,666  |  **Created:** 2026-03-11

**Background:** Gstack is a brand-new repository by Garry Tan, the current Y Combinator president, that packages twelve opinionated workflow skills for Claude Code as slash commands. Created just four days ago, it has already amassed nearly 18,000 stars, reflecting Tan's massive audience and the hunger for curated agentic workflows.

**Problem it solves:** Claude Code is powerful but generic out of the box — it takes requests literally, gives inconsistent review depth, and cannot see your running app. Gstack provides role-specific slash commands (CEO plan review, design review, paranoid code review, one-command shipping, browser QA) that enforce structured, repeatable workflows.

**Why another one?** The celebrity-founder angle and the extreme specificity of each skill set it apart. Rather than a general-purpose framework, gstack is a single opinionated configuration that mirrors how one high-profile builder actually works, which gives it an authenticity that prompt template libraries lack.

---

## 2. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers.

**Language:** Shell  |  **Stars:** 46,473  |  **Forks:** 6,940  |  **Score:** 14,520  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski is a growing collection of meticulously crafted AI agent personas, born from a Reddit thread and months of iteration. Each agent is a specialized expert with a unique personality, communication style, defined processes, and measurable deliverables, distributed as shell scripts and prompt configurations for Claude Code.

**Problem it solves:** Teams adopting AI agents for professional tasks need role-specific system prompts and workflow definitions. Building these from scratch for each domain — frontend, community management, content strategy — requires significant prompt engineering effort that most teams would rather skip.

**Why another one?** The personality-driven approach makes each agent entertaining and distinctive rather than a generic prompt template. Agents have names, quirks, and strong opinions, which drives organic sharing and makes the collection function more like an agency roster than a configuration library.

---

## 3. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 17,254  |  **Forks:** 1,525  |  **Score:** 8,554  |  **Created:** 2025-10-31

**Background:** This repository by Shan Raisshan is a comprehensive guide to Claude Code best practices, covering the Command-Agent-Skill orchestration workflow, implementation patterns, and practical tips. It is kept continuously up to date (current with Claude Code v2.1.77) and includes visual guides and implementation examples.

**Problem it solves:** Claude Code's capabilities are extensive but poorly documented in terms of real-world workflow design. This repository bridges the gap between Anthropic's official documentation and how experienced practitioners actually structure their agent workflows for maximum effectiveness.

**Why another one?** While many Claude Code tips circulate on social media, this repository consolidates them into a structured, versioned reference with working implementations. Its orchestration workflow documentation — showing how commands, agents, and skills compose — fills a specific gap that scattered blog posts and tweets cannot.

---

## 4. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 85,570  |  **Forks:** 6,721  |  **Score:** 6,905  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, built on composable skills that trigger automatically. With over 85,000 stars, it has become one of the most popular agentic development frameworks. The system enforces a structured flow: spec extraction, design review, implementation planning, and subagent-driven development with continuous inspection.

**Problem it solves:** Coding agents tend to jump straight into writing code without understanding requirements, leading to implementations that miss the real product need. Superpowers forces a disciplined sequence — spec, plan, implement, review — that keeps agents on track for hours of autonomous work.

**Why another one?** Superpowers emphasizes true red/green TDD, YAGNI, and DRY principles in its implementation plans, targeting them at "an enthusiastic junior engineer with poor taste." This deliberate lowering of the assumed execution quality produces more robust plans than frameworks that assume an ideal agent.

---

## 5. [OpenViking](https://github.com/volcengine/OpenViking)
> OpenViking is an open-source context database designed specifically for AI Agents. It unifies the management of context (memory, resources, and skills) through a file system paradigm.

**Language:** Python  |  **Stars:** 12,376  |  **Forks:** 847  |  **Score:** 5,270  |  **Created:** 2026-01-05

**Background:** OpenViking is an open-source context database from Volcengine (ByteDance's cloud division) designed specifically for AI agents. It unifies the management of memory, resources, and skills that agents need through a file system paradigm, enabling hierarchical context delivery and self-evolving agent capabilities.

**Problem it solves:** Agent developers face fragmented context — memories live in code, resources in databases, and skills in separate configs. OpenViking consolidates these into a single filesystem-like interface, making context composable, hierarchical, and queryable without juggling multiple storage backends.

**Why another one?** Backed by ByteDance's engineering resources, OpenViking addresses context management at a level of abstraction that most agent frameworks ignore. The filesystem paradigm is intuitive for developers and makes context shareable across agents, which is critical for multi-agent systems like those built on OpenClaw.

---

## 6. [system-design-academy](https://github.com/systemdesign42/system-design-academy)
> If you want to become good at system design, join this newsletter now

**Language:** N/A  |  **Stars:** 23,256  |  **Forks:** 2,876  |  **Score:** 4,198  |  **Created:** 2024-02-15

**Background:** System Design Academy is a curated collection of system design case studies and fundamentals, organized alphabetically by company and technology. It serves as a companion resource to the systemdesign.one newsletter and covers real-world architectures from dozens of major companies.

**Problem it solves:** System design interview preparation typically involves scattered resources of varying quality. This repository provides a single, well-organized index of case studies drawn from actual company engineering blogs, bridging the gap between textbook concepts and production architectures.

**Why another one?** Unlike general system design courses, this repository is organized as a company-indexed reference, letting candidates study the specific architectures of companies they are interviewing at. The newsletter integration provides ongoing updates as new case studies are published.

---

## 7. [CLI-Anything](https://github.com/HKUDS/CLI-Anything)
> CLI-Anything: Making ALL Software Agent-Native

**Language:** Python  |  **Stars:** 16,206  |  **Forks:** 1,374  |  **Score:** 4,064  |  **Created:** 2026-03-08

**Background:** CLI-Anything from the HKU Data Science lab converts any GUI application into a CLI that AI agents can operate. Created just a week ago, it has rapidly gained over 16,000 stars. The project demonstrates conversions across 13 applications with 1,588 passing tests, outputting both JSON and human-readable formats.

**Problem it solves:** Today's software is built for human users with graphical interfaces, but tomorrow's users are increasingly AI agents that need programmatic access. CLI-Anything bridges this gap by automatically generating CLI wrappers for existing software, making any application agent-operable without modifying its source.

**Why another one?** Most agent-tool integration approaches require the software author to build an API or plugin. CLI-Anything works from the outside in, wrapping existing applications without their cooperation. This makes the entire installed software ecosystem immediately available to agents rather than waiting for each vendor to build integrations.

---

## 8. [browser](https://github.com/lightpanda-io/browser)
> Lightpanda: the headless browser designed for AI and automation

**Language:** Zig  |  **Stars:** 18,080  |  **Forks:** 672  |  **Score:** 3,997  |  **Created:** 2023-02-07

**Background:** Lightpanda is a headless browser built from scratch in Zig — not a Chromium fork or WebKit patch. It is designed specifically for AI agents and automation workloads, offering dramatically faster execution times and lower memory usage than traditional headless browsers in benchmarks against Puppeteer on Chromium.

**Problem it solves:** Headless Chromium is resource-hungry and slow for automation at scale. Lightpanda provides a purpose-built alternative that supports JavaScript execution and Web APIs while consuming a fraction of the resources, making large-scale web scraping and agent browsing economically viable.

**Why another one?** Writing a browser engine from scratch in Zig is an extraordinarily ambitious approach that yields performance characteristics impossible to achieve by patching existing engines. The Zig language choice gives precise memory control without a garbage collector, directly translating to the low-memory, high-throughput profile that automation workloads demand.

---

## 9. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 38,849  |  **Forks:** 5,377  |  **Score:** 3,567  |  **Created:** 2026-03-06

**Background:** Andrej Karpathy's autoresearch gives an AI agent a small but real LLM training setup (based on nanochat) and lets it experiment autonomously overnight. The agent modifies code, trains for 5 minutes, evaluates results, keeps or discards changes, and repeats. The researcher wakes up to a log of experiments and hopefully a better model.

**Problem it solves:** The tedious cycle of hypothesis, code modification, experiment, and analysis that consumes a researcher's days. Autoresearch runs this loop continuously while the human is away, accelerating the pace of empirical ML research.

**Why another one?** The key insight is that researchers do not touch the Python training code directly — instead they program Markdown files (program.md) that provide context and directives to the AI agents. This separation of concerns between research direction (human) and execution (agent) is a genuinely novel workflow for ML experimentation.

---

## 10. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything

**Language:** Python  |  **Stars:** 26,759  |  **Forks:** 3,202  |  **Score:** 3,180  |  **Created:** 2025-11-26

**Background:** MiroFish by Shanda Group is a swarm intelligence prediction engine that applies bio-inspired collective intelligence algorithms — modeled on fish school behavior — to make predictions across diverse domains. With nearly 27,000 stars, it has established itself as a credible alternative to monolithic prediction models.

**Problem it solves:** Traditional prediction systems rely on single large models that are expensive to retrain and brittle to distribution shifts. MiroFish distributes prediction across a swarm of simple agents, each processing different signals, then aggregates their outputs for more robust and extensible forecasting.

**Why another one?** The swarm intelligence approach offers a genuinely different architectural paradigm from the transformer-dominant landscape. Its Docker-ready deployment and support for financial, weather, and social trend prediction domains make it practical rather than purely academic.

---

## 11. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash is all you need - A nano Claude Code-like agent, built from 0 to 1

**Language:** TypeScript  |  **Stars:** 27,884  |  **Forks:** 4,878  |  **Score:** 3,019  |  **Created:** 2025-06-29

**Background:** Learn Claude Code by shareAI-lab is an educational project that builds a minimal Claude Code-like agent from scratch, demonstrating that the core of an AI coding agent is fundamentally a model with bash access. The repository emphasizes that "an agent is a model, not a framework" and traces the lineage from DeepMind's DQN to modern coding agents.

**Problem it solves:** Developers who want to understand how agentic coding tools work internally find existing implementations too complex to study. This project strips the concept to its essence, making the architecture legible and reproducible.

**Why another one?** The philosophical stance — that agents are trained models, not prompt chains or drag-and-drop workflows — provides a clear pedagogical framework. By building from zero to one, it demystifies what commercial tools like Claude Code actually do under the hood.

---

## 12. [defuddle](https://github.com/kepano/defuddle)
> Get the main content of any page as Markdown.

**Language:** HTML  |  **Stars:** 5,076  |  **Forks:** 193  |  **Score:** 2,834  |  **Created:** 2025-02-27

**Background:** Defuddle by Kepano (creator of Obsidian Web Clipper) extracts the main content from web pages by removing clutter like comments, sidebars, headers, and footers. It works as a drop-in replacement for Mozilla Readability, running in both browser and Node.js environments with any DOM implementation.

**Problem it solves:** Web pages are cluttered with navigation, ads, and sidebars that make content extraction noisy. Defuddle cleans pages down to their primary content, outputting clean HTML or Markdown suitable for note-taking tools and AI ingestion pipelines.

**Why another one?** Compared to Mozilla Readability, Defuddle is more forgiving (removes fewer uncertain elements), provides consistent output for footnotes, math, and code blocks, uses mobile styles to detect unnecessary elements, and extracts richer metadata including schema.org data. Its origin in Obsidian Web Clipper means it has been battle-tested on diverse real-world pages.

---

## 13. [system-design-101](https://github.com/ByteByteGoHq/system-design-101)
> Explain complex systems using visuals and simple terms. Help you prepare for system design interviews.

**Language:** N/A  |  **Stars:** 81,160  |  **Forks:** 8,886  |  **Score:** 2,778  |  **Created:** 2023-09-18

**Background:** ByteByteGo's System Design 101 is an 81,000-star reference that explains complex systems using visuals and simple terms. Created by the team behind the popular ByteByteGo newsletter and YouTube channel, it covers API design, database internals, caching strategies, microservices patterns, and much more through clear diagrams.

**Problem it solves:** System design concepts are abstract and hard to internalize from text alone. This repository uses visual explanations — architecture diagrams, flow charts, comparison tables — to make concepts like load balancing, database sharding, and message queues immediately graspable.

**Why another one?** The visual-first approach is the key differentiator. While most system design resources are text-heavy, ByteByteGo's diagrams have become a recognizable visual language in the engineering community. The companion YouTube channel and newsletter create a multi-format learning experience.

---

## 14. [Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders)
> Practical marketing resources to get the first 10 / 100 / 1000 users for your SaaS / App / Startup

**Language:** N/A  |  **Stars:** 4,761  |  **Forks:** 484  |  **Score:** 2,576  |  **Created:** 2025-05-19

**Background:** Marketing for Founders by EdoStra is a curated collection of practical marketing resources specifically targeted at technical founders building their first startup. It covers launch platforms, Product Hunt strategy, social media marketing, cold outreach, SEO, LLM SEO, Reddit marketing, email marketing, and more.

**Problem it solves:** Most marketing advice targets VC-funded startups with large budgets scaling to $1M ARR. Technical founders moving their first steps need actionable, zero-budget tactics to find their first 10, 100, and 1,000 users — and this resource addresses that specific stage.

**Why another one?** The stage-specific focus (first users, not scaling) and the zero-budget constraint make it uniquely relevant to bootstrapped founders. The inclusion of LLM SEO and AI-specific marketing channels reflects the current landscape where traditional SEO alone is insufficient.

---

## 15. [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
> Official, Anthropic-managed directory of high quality Claude Code Plugins.

**Language:** Python  |  **Stars:** 11,927  |  **Forks:** 1,153  |  **Score:** 2,487  |  **Created:** 2025-11-20

**Background:** This is Anthropic's official curated directory of Claude Code plugins, containing both internal plugins developed by Anthropic and vetted external plugins from partners and the community. Plugins can be installed directly via Claude Code's plugin system using slash commands.

**Problem it solves:** As the Claude Code plugin ecosystem grows, users need a trusted source for discovering and installing plugins that meet quality and security standards. This directory provides that curation layer with a standard plugin structure and submission process.

**Why another one?** Being the official Anthropic-managed directory gives it an authority and trust level that community-driven alternatives cannot match. The structured submission process and quality review ensure a baseline of reliability that matters when plugins have access to your development environment.

---

## 16. [CloakBrowser](https://github.com/CloakHQ/CloakBrowser)
> Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed.

**Language:** Python  |  **Stars:** 696  |  **Forks:** 51  |  **Score:** 2,420  |  **Created:** 2026-02-22

**Background:** CloakBrowser is a stealth Chromium build that applies source-level fingerprint patches to pass all major bot detection tests (30/30). It serves as a drop-in replacement for Playwright, available via PyPI, npm, and Docker, making it accessible across Python and Node.js ecosystems.

**Problem it solves:** Standard headless browsers are immediately detected by anti-bot systems, breaking automation and scraping workflows. CloakBrowser patches Chromium at the source level rather than using runtime JavaScript overrides, making its stealth properties fundamentally harder to detect.

**Why another one?** Source-level patching is a more thorough approach than the runtime fingerprint spoofing used by tools like Puppeteer-extra-plugin-stealth. The drop-in Playwright compatibility means existing automation code works without modification, lowering the migration barrier to near zero.

---

## 17. [LinkSwift](https://github.com/hmjz100/LinkSwift)
> A JavaScript-based cloud drive file download URL extraction tool, supporting Baidu, Alibaba, China Mobile, Tianyi, Xunlei, Quark, UC, and 123 cloud drives.

**Language:** JavaScript  |  **Stars:** 13,303  |  **Forks:** 762  |  **Score:** 2,414  |  **Created:** 2022-08-10

**Background:** LinkSwift is a JavaScript userscript tool that extracts direct download links from eight major Chinese cloud storage platforms including Baidu Netdisk, Alibaba Cloud Drive, and Quark. It is a fork of the popular "cloud drive direct link download assistant" with continued maintenance and expanded platform support.

**Problem it solves:** Chinese cloud storage services throttle downloads through their native clients and require app installation. LinkSwift bypasses these restrictions by extracting direct download URLs, enabling full-speed downloads through any download manager.

**Why another one?** LinkSwift supports eight platforms in a single script — broader coverage than most alternatives. Its continued maintenance matters because cloud platforms frequently change their APIs and detection methods, and an actively updated tool is essential for ongoing functionality.

---

## 18. [heretic](https://github.com/p-e-w/heretic)
> Fully automatic censorship removal for language models

**Language:** Python  |  **Stars:** 14,817  |  **Forks:** 1,505  |  **Score:** 2,388  |  **Created:** 2025-09-21

**Background:** Heretic by p-e-w is a tool that removes safety alignment (censorship) from transformer-based language models without expensive post-training. It combines an advanced implementation of directional ablation ("abliteration") with a TPE-based parameter optimizer powered by Optuna to find high-quality decensoring parameters automatically.

**Problem it solves:** Researchers and developers who need uncensored model outputs face a choice between expensive fine-tuning or manual prompt engineering. Heretic automates the process completely, co-minimizing refusals and KL divergence from the original model to preserve quality while removing restrictions.

**Why another one?** The fully automatic approach is the differentiator — Heretic finds optimal abliteration parameters by itself, requiring no manual tuning or labeled data. The KL divergence preservation ensures the decensored model retains as much of the original model's capabilities as possible, avoiding the quality degradation common in cruder approaches.

---

## 19. [system-design](https://github.com/karanpratapsingh/system-design)
> Learn how to design systems at scale and prepare for system design interviews

**Language:** N/A  |  **Stars:** 42,074  |  **Forks:** 5,340  |  **Score:** 2,270  |  **Created:** 2022-08-15

**Background:** Karan Pratap Singh's system design course is a comprehensive, free resource covering everything from IP and OSI fundamentals through databases, distributed systems, and real-world case studies. With 42,000 stars, it has become one of the most popular system design learning resources on GitHub, also available on Leanpub as an ebook.

**Problem it solves:** System design interviews require broad knowledge across networking, databases, caching, messaging, and architectural patterns. This course provides a structured progression from fundamentals to advanced topics in a single, self-contained repository.

**Why another one?** The structured chapter progression (fundamentals, databases, distributed systems, case studies) mirrors an actual course curriculum rather than a random collection of articles. The free availability on GitHub with an optional paid ebook makes it accessible while supporting the author.

---

## 20. [public-apis](https://github.com/public-apis/public-apis)
> A collective list of free APIs

**Language:** Python  |  **Stars:** 411,142  |  **Forks:** 44,435  |  **Score:** 2,159  |  **Created:** 2016-03-20

**Background:** Public APIs is one of the most-starred repositories on all of GitHub with over 411,000 stars. It is a community-curated list of free APIs spanning categories from finance to weather to entertainment, maintained over nearly a decade of continuous contributions.

**Problem it solves:** Developers building new projects need to discover free API services for common functionality — geocoding, currency exchange, weather data, authentication. This repository serves as the canonical directory, saving hours of research per project.

**Why another one?** At 411,000 stars and 10 years of curation, public-apis has no real competitor in scope or community trust. Its continued appearance on trending lists reflects a steady stream of new developers discovering it for the first time.

---

## 21. [awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts)
> World's largest Nano Banana Pro prompt library — 10,000+ curated prompts with preview images, 16 languages.

**Language:** TypeScript  |  **Stars:** 9,098  |  **Forks:** 929  |  **Score:** 2,112  |  **Created:** 2025-11-23

**Background:** This repository by YouMind-OpenLab is a curated collection of over 10,000 creative prompts for Google's Nano Banana Pro image generation model, available in 16 languages. It includes preview images for each prompt and is updated via automated GitHub Actions workflows.

**Problem it solves:** AI image generation prompt engineering requires extensive experimentation to discover what produces good results with a specific model. This library provides thousands of tested, community-sourced prompts with preview images, letting users find effective starting points instantly.

**Why another one?** The scale (10,000+ prompts) and the inclusion of preview images for each prompt set it apart from smaller prompt collections. Multi-language support in 16 languages makes it accessible to a global audience rather than just English speakers.

---

## 22. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
> LLM-driven A/H/US stock intelligent analyzer with multi-source data, real-time news, LLM decision dashboard, and multi-channel push notifications. Zero cost.

**Language:** Python  |  **Stars:** 20,639  |  **Forks:** 21,366  |  **Score:** 2,053  |  **Created:** 2026-01-10

**Background:** Daily Stock Analysis by Zhu Linsen is an AI-powered stock analysis system that covers A-shares, Hong Kong stocks, and US markets. It runs on GitHub Actions for zero infrastructure cost, combining multi-source market data with real-time news analysis through LLMs to produce daily decision dashboards pushed to WeChat Work, Feishu, Telegram, Discord, or email.

**Problem it solves:** Individual investors lack the time and tools to synthesize market data, news, and technical indicators across multiple markets daily. This system automates the entire pipeline — data collection, AI analysis, and delivery — at zero running cost using free-tier cloud services.

**Why another one?** The zero-cost angle (GitHub Actions + free LLM APIs) removes the hosting barrier entirely. Supporting three major market regions (A-shares, HK, US) in a single system with multi-channel push notifications makes it more comprehensive than single-market alternatives.

---

## 23. [daytona](https://github.com/daytonaio/daytona)
> Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code

**Language:** TypeScript  |  **Stars:** 65,179  |  **Forks:** 5,080  |  **Score:** 1,963  |  **Created:** 2024-02-06

**Background:** Daytona provides secure, elastic infrastructure for running AI-generated code, with 65,000 stars making it one of the most popular developer infrastructure projects. It offers sandboxed execution environments that can spin up on demand, providing the isolation layer between AI code generation and production systems.

**Problem it solves:** AI agents generate code that needs to be executed safely — untested, potentially buggy, and possibly malicious code should not run directly on production infrastructure. Daytona provides sandboxed environments with resource controls and security boundaries.

**Why another one?** With 65,000 stars and active development, Daytona has become the default answer to "where do I run AI-generated code?" Its elastic scaling means environments spin up in seconds and cost nothing when idle, matching the bursty workload pattern of agentic development.

---

## 24. [InsForge](https://github.com/InsForge/InsForge)
> Give agents everything they need to ship fullstack apps. The backend built for agentic development.

**Language:** TypeScript  |  **Stars:** 4,600  |  **Forks:** 474  |  **Score:** 1,961  |  **Created:** 2025-07-29

**Background:** InsForge is a backend platform built specifically for agentic development, providing everything AI agents need to ship fullstack applications. It offers a Docker-based local setup, SDK packages on npm, and integration paths for popular AI coding tools including Cursor.

**Problem it solves:** AI coding agents can generate frontend and backend code but struggle with the infrastructure layer — databases, authentication, deployment pipelines. InsForge provides a pre-configured backend stack that agents can deploy to without manual infrastructure setup.

**Why another one?** The "built for agentic development" positioning means every API surface is designed for programmatic access rather than human dashboards. The one-click Cursor integration and Docker Compose setup reflect an understanding that the developer experience must be agent-friendly from the start.

---

## 25. [Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
> Official code repo for the O'Reilly Book - "Hands-On Large Language Models"

**Language:** Jupyter Notebook  |  **Stars:** 23,895  |  **Forks:** 5,530  |  **Score:** 1,936  |  **Created:** 2024-06-28

**Background:** This is the official code repository for the O'Reilly book "Hands-On Large Language Models" by Jay Alammar and Maarten Grootendorst. It contains Jupyter notebooks that accompany each chapter, along with a companion DeepLearning.AI short course on how transformers and LLMs work.

**Problem it solves:** Understanding LLMs requires moving from theory to working code, but setting up experiments from scratch is time-consuming. These notebooks provide tested, runnable implementations that match the book's explanations, letting learners experiment immediately.

**Why another one?** The combination of a published O'Reilly book, a DeepLearning.AI course, and open-source notebooks creates a uniquely comprehensive learning path. The authors' profiles (Alammar's legendary visual explanations and Grootendorst's BERTopic work) lend deep credibility to the content.

---

> **Day's theme:** Claude Code tooling dominates the chart as the agentic development ecosystem matures — purpose-built skills, plugins, best practices, and infrastructure projects are converging to make AI-driven software development a structured discipline rather than ad hoc prompting.
