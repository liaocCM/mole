# Trendshift Report — 2026-03-09
**Total:** 25 repositories

---

## 1. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 8,719  |  **Forks:** 1,154  |  **Score:** 33,837  |  **Created:** 2026-03-06

**Background:** Autoresearch is Andrej Karpathy's experiment in autonomous AI-driven ML research. Launched March 6, 2026, the project gives an AI agent a real LLM training setup (based on nanochat) and lets it run unsupervised experiments overnight on a single GPU. The agent formulates hypotheses, modifies training code, runs experiments, analyzes results, and proposes next steps — all without human intervention.

**Problem it solves:** ML research involves a tedious cycle of hypothesis formation, code modification, experiment execution, and result analysis that keeps researchers waiting on GPU runs. Autoresearch automates this entire loop, allowing the research process to continue 24/7 while the human researcher sleeps, eats, or works on higher-level strategy.

**Why another one?** Karpathy's framing is deliberately provocative: the README's fictional future narrative about AI agents taking over research entirely positions this as the origin story of autonomous AI research. The combination of Karpathy's name recognition and the genuinely novel concept of letting agents run real training experiments (not just toy benchmarks) explains its explosive score of 33,837.

---

## 2. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers.

**Language:** Shell  |  **Stars:** 18,396  |  **Forks:** 2,842  |  **Score:** 11,336  |  **Created:** 2025-10-13

**Background:** Agency Agents provides a library of pre-built AI agent personas by Mark Sitarzewski, each designed as a specialized professional with defined personality, processes, and deliverables. The collection covers roles across development, marketing, community management, and creative work, distributed as shell scripts and prompt configurations.

**Problem it solves:** Creating effective AI agents for specific professional roles requires significant prompt engineering effort. Agency Agents provides battle-tested role definitions that teams can deploy immediately, skipping the iteration cycle of crafting and refining system prompts for each new use case.

**Why another one?** Its score nearly quadrupled from the previous day (2,972 to 11,336), suggesting a viral moment — likely driven by social media sharing of specific agent personas. The collection's breadth and the entertaining personality injection in each agent definition make it highly shareable content.

---

## 3. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies

**Language:** TypeScript  |  **Stars:** 9,517  |  **Forks:** 1,062  |  **Score:** 8,143  |  **Created:** 2026-03-02

**Background:** Paperclip is an open-source business orchestration platform that automates entire company operations through coordinated AI agents. Launched a week ago, it has maintained strong momentum with its score rising from 5,842 to 8,143 day-over-day, reflecting sustained interest in the zero-human company concept.

**Problem it solves:** Small businesses require dozens of operational workflows — customer support, invoicing, inventory management — each traditionally requiring human operators or disconnected automation tools. Paperclip provides a unified orchestration layer where AI agents handle these workflows end-to-end.

**Why another one?** Paperclip's continued strong performance on day two confirms that the "zero-human company" framing resonates beyond novelty. The project occupies a unique niche between developer-focused agent frameworks (which require coding to use) and vertical SaaS tools (which automate only one function), offering full-stack business automation.

---

## 4. [neko](https://github.com/m1k1o/neko)
> A self hosted virtual browser that runs in docker and uses WebRTC.

**Language:** Go  |  **Stars:** 18,739  |  **Forks:** 1,296  |  **Score:** 7,261  |  **Created:** 2020-03-14

**Background:** Neko is a self-hosted virtual browser that runs inside Docker containers and streams the browser UI to clients via WebRTC. Created by m1k1o in March 2020, it supports collaborative browsing where multiple users can view and interact with the same browser session. The project has grown to nearly 19,000 stars over its six-year history.

**Problem it solves:** Remote browser isolation, collaborative browsing sessions, and secure access to web applications from untrusted networks all require streaming a browser instance from a server. Neko packages this capability into a single Docker container with WebRTC-based low-latency streaming, making it trivial to deploy.

**Why another one?** Neko's sudden surge in score likely reflects its utility as a browser sandbox for AI agents. As coding agents increasingly need to interact with web UIs, a containerized browser accessible via API becomes essential infrastructure. The project's Docker-native design makes it a natural fit for agent orchestration platforms.

---

## 5. [generative-ai](https://github.com/GoogleCloudPlatform/generative-ai)
> Sample code and notebooks for Generative AI on Google Cloud, with Gemini on Vertex AI

**Language:** Jupyter Notebook  |  **Stars:** 14,626  |  **Forks:** 3,912  |  **Score:** 6,788  |  **Created:** 2023-05-05

**Background:** Google Cloud's official repository of generative AI samples and notebooks for Vertex AI. The Gemini 3.1 Pro launch continues to drive traffic to this repository, which serves as the canonical starting point for developers adopting the latest model capabilities.

**Problem it solves:** Each Gemini model release introduces new capabilities and API changes. This repository provides immediately runnable notebooks that demonstrate the new features, reducing the gap between announcement and practical adoption.

**Why another one?** Its score jumped from 4,046 to 6,788 day-over-day, suggesting the Gemini 3.1 Pro launch is still in its early adoption wave. As the official Google source, it captures developer attention whenever the model family is updated.

---

## 6. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything

**Language:** Python  |  **Stars:** 10,216  |  **Forks:** 1,069  |  **Score:** 6,126  |  **Created:** 2025-11-26

**Background:** MiroFish is a swarm intelligence prediction engine backed by Shanda Group that applies bio-inspired collective intelligence to prediction tasks across financial markets, weather, and social trends. It aggregates signals from multiple lightweight agents, each processing different data sources.

**Problem it solves:** Monolithic prediction models are expensive to train and fragile to distribution shifts. MiroFish distributes the prediction task across a swarm of simple agents, making the system more robust and extensible without retraining the entire model.

**Why another one?** MiroFish's score increased from 3,821 to 6,126, indicating growing momentum. The swarm intelligence approach remains genuinely novel in a landscape dominated by transformer-based architectures, and its practical applicability to financial prediction gives it appeal beyond the ML research community.

---

## 7. [canopy](https://github.com/canopy-network/canopy)
> The official go implementation of the Canopy Network protocol

**Language:** Go  |  **Stars:** 4,262  |  **Forks:** 9,293  |  **Score:** 5,782  |  **Created:** 2024-10-30

**Background:** Canopy is the official Go implementation of the Canopy Network protocol, a blockchain/decentralized infrastructure project. The repository includes both the protocol node implementation and a Next.js web dashboard. Despite having only 4,262 stars, its 9,293 forks — an unusually high fork-to-star ratio — suggest significant developer activity around the protocol.

**Problem it solves:** Canopy Network provides decentralized infrastructure services, and this implementation gives node operators and developers a reference client to participate in the network. The bundled web dashboard provides visibility into network state and node operations.

**Why another one?** The extremely high fork-to-star ratio (2.18:1 vs the typical 0.1:1) is the notable data point here. This pattern typically indicates either airdrop farming (forks for token eligibility) or a protocol that requires node operators to fork and customize the codebase. Its appearance on the trending list likely reflects a network event or incentive program.

---

## 8. [impeccable](https://github.com/pbakaus/impeccable)
> The design language that makes your AI harness better at design.

**Language:** JavaScript  |  **Stars:** 2,772  |  **Forks:** 105  |  **Score:** 5,021  |  **Created:** 2025-11-16

**Background:** Impeccable is a design skill and vocabulary system by Paul Bakaus that improves how AI coding agents handle frontend design. It builds on Anthropic's official frontend-design skill with deeper expertise, 17 specialized commands, and curated anti-patterns that counteract the generic template bias baked into LLM training data.

**Problem it solves:** LLMs trained on public web data reproduce the same design mistakes: Inter font, purple gradients, cards nested in cards, gray text on colored backgrounds. Impeccable provides specific design rules, reference files, and anti-pattern documentation that steer agents away from these cliches toward more thoughtful, varied design decisions.

**Why another one?** While Anthropic's frontend-design skill provides a baseline, Impeccable adds substantially more depth with 7 domain-specific reference files and explicit anti-pattern documentation. It targets the specific problem of LLM design homogeneity rather than general UI component generation.

---

## 9. [pm-skills](https://github.com/phuryn/pm-skills)
> PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, execution, launch, and growth.

**Language:** —  |  **Stars:** 5,646  |  **Forks:** 523  |  **Score:** 4,645  |  **Created:** 2026-03-01

**Background:** PM Skills Marketplace provides over 65 product management skills and 36 chained workflows organized across 8 plugins, designed for Claude Code and Cowork. It covers the full product lifecycle from discovery through strategy, execution, launch, and growth, with each skill invokable as a slash command.

**Problem it solves:** Product managers perform repetitive analytical and strategic tasks — competitive analysis, user story mapping, prioritization frameworks — that follow well-defined templates. PM Skills encodes these templates as agent skills, allowing a PM to invoke `/discover` for new ideas or `/strategy` for strategic clarity instead of starting from a blank document.

**Why another one?** PM Skills extends the agent skills paradigm beyond engineering into product management, which is notably underserved in the current skills ecosystem. The chained workflow concept — where one skill's output feeds into another — adds composability that individual skills lack.

---

## 10. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.

**Language:** —  |  **Stars:** 33,181  |  **Forks:** 3,144  |  **Score:** 4,534  |  **Created:** 2026-01-25

**Background:** VoltAgent's curated catalog of over 5,400 OpenClaw skills continues to trend as the primary discovery layer for the OpenClaw skills ecosystem. The repository organizes skills by category and maintains quality filters that the official registry does not provide.

**Problem it solves:** The official OpenClaw Skills Registry lists thousands of skills without meaningful categorization or quality filtering. This curated collection makes discovery practical by organizing skills into functional categories and removing abandoned or low-quality entries.

**Why another one?** Persistent demand for OpenClaw skill discovery drives its recurring presence on trending lists. Each new batch of skills added to the registry creates a new wave of users searching for curated recommendations.

---

## 11. [t3code](https://github.com/pingdotgg/t3code)
> A minimal web GUI for coding agents

**Language:** TypeScript  |  **Stars:** 4,302  |  **Forks:** 476  |  **Score:** 4,235  |  **Created:** 2026-02-08

**Background:** T3 Code is a minimal web GUI for coding agents from Ping (the T3 Stack creators). Currently Codex-first with Claude Code support planned, it provides a browser-based interface for managing and interacting with terminal-based coding agents. Available as both an npx command and a downloadable desktop app.

**Problem it solves:** Terminal-based coding agents like Codex and Claude Code are powerful but lack visual interfaces for managing conversations, reviewing outputs, and navigating project context. T3 Code wraps these agents in a clean web UI without replacing their underlying capabilities.

**Why another one?** The T3 Stack team brings credibility in developer tooling, and the "minimal" positioning differentiates it from heavier IDE integrations. Supporting multiple agent backends (Codex now, Claude Code soon) makes it a neutral GUI layer rather than a platform-specific tool.

---

## 12. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 289,626  |  **Forks:** 54,924  |  **Score:** 3,972  |  **Created:** 2025-11-24

**Background:** OpenClaw maintains its position as the most-starred personal AI assistant on GitHub at nearly 290,000 stars. The project continues to benefit from the growing ecosystem of skills, use-case collections, and derivative projects that all reference back to the main repository.

**Problem it solves:** A fully self-hosted, extensible AI assistant that users own and control, with a plugin architecture enabling thousands of community-built skills.

**Why another one?** OpenClaw is not "another one" — it is the platform that the majority of this week's trending repositories build upon. Its persistent trending reflects ecosystem momentum rather than any single feature release.

---

## 13. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**Language:** JavaScript  |  **Stars:** 69,024  |  **Forks:** 8,618  |  **Score:** 3,866  |  **Created:** 2026-01-18

**Background:** Everything Claude Code (ECC) continues its strong presence as a comprehensive optimization system for AI coding agents. With nearly 70,000 stars, it provides skills, instincts, memory management, and security configurations across multiple agent platforms via installable npm packages.

**Problem it solves:** Default coding agent configurations lack opinionated settings for research-first development, security hardening, and persistent memory. ECC bundles these into cross-platform packages that transform generic agents into tuned development partners.

**Why another one?** ECC's holistic approach — covering instincts (behavioral modifications), not just skills (task capabilities) — remains its primary differentiator. Its npm distribution model continues to drive adoption.

---

## 14. [ui](https://github.com/shadcn-ui/ui)
> A set of beautifully-designed, accessible components and a code distribution platform.

**Language:** TypeScript  |  **Stars:** 108,588  |  **Forks:** 8,067  |  **Score:** 3,009  |  **Created:** 2023-01-04

**Background:** shadcn/ui continues to be the default component system for new web projects, particularly those scaffolded by AI coding agents. Its code-generation distribution model — copying components into your project rather than installing a dependency — aligns perfectly with how AI agents build applications.

**Problem it solves:** Traditional component libraries impose styling opinions and upgrade cycles. shadcn/ui distributes source code, giving developers full ownership and customization freedom.

**Why another one?** shadcn/ui trends persistently because AI coding agents use it as their default component library when building web applications. Every new project an agent scaffolds adds a new user to the ecosystem.

---

## 15. [symphony](https://github.com/openai/symphony)
> Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents.

**Language:** Elixir  |  **Stars:** 9,439  |  **Forks:** 653  |  **Score:** 2,965  |  **Created:** 2026-02-26

**Background:** OpenAI's Elixir-based orchestration layer for Codex that monitors project management boards for tasks and spawns isolated agents to implement them. Agents deliver pull requests with CI status, review feedback, complexity analysis, and walkthrough videos as proof of work.

**Problem it solves:** Managing coding agents still requires human supervision for task assignment, output review, and workflow coordination. Symphony automates this management layer by connecting directly to project boards and handling the full cycle from ticket to reviewed PR.

**Why another one?** The Elixir choice provides strong concurrency for managing multiple agent runs simultaneously. The "proof of work" model — agents must provide evidence of quality, not just code — addresses the trust problem in autonomous agent development.

---

## 16. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:** —  |  **Stars:** 22,126  |  **Forks:** 1,817  |  **Score:** 2,759  |  **Created:** 2026-02-08

**Background:** A community-curated collection of 36 real-world OpenClaw use cases across productivity, health, education, and personal automation. It provides practical templates and workflow inspiration for new OpenClaw users.

**Problem it solves:** The gap between what an AI assistant can do and what real people actually use it for. This collection documents specific workflows and setups that community members have validated in practice.

**Why another one?** Complements skills catalogs by focusing on outcomes rather than capabilities. Trends alongside the broader OpenClaw ecosystem growth.

---

## 17. [Siftly](https://github.com/viperrcrypto/Siftly)
> Local Twitter/X bookmark organizer with AI categorization and mindmap visualization

**Language:** TypeScript  |  **Stars:** 1,279  |  **Forks:** 102  |  **Score:** 2,638  |  **Created:** 2026-03-04

**Background:** Siftly is a self-hosted Twitter/X bookmark manager with AI categorization and interactive mindmap visualization. Built on Next.js 16 with SQLite for fully local storage, it launched a few days ago and is gaining traction as a privacy-respecting alternative to cloud bookmark services.

**Problem it solves:** Twitter bookmarks are an unsearchable, unorganized flat list. Siftly imports, categorizes, and visualizes them as connected mindmaps, transforming a neglected feature into a useful knowledge base.

**Why another one?** The mindmap visualization sets it apart from folder-based bookmark managers. Running entirely locally with SQLite appeals to users concerned about sharing their bookmark data with third-party services.

---

## 18. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript in-page GUI agent. Control web interfaces with natural language.

**Language:** TypeScript  |  **Stars:** 2,399  |  **Forks:** 194  |  **Score:** 2,495  |  **Created:** 2025-09-23

**Background:** Alibaba's in-page GUI automation agent that runs inside the web page's JavaScript runtime, using vision-language models to translate natural language instructions into DOM manipulations. Unlike external browser automation tools, it operates from within the page context.

**Problem it solves:** Browser automation through external drivers (Selenium, Playwright) requires brittle CSS selectors that break on UI changes. Page Agent uses visual understanding to identify and interact with elements, making automation more resilient.

**Why another one?** The in-page architecture gives it direct access to JavaScript state and event handlers, enabling more precise interactions than screenshot-based external approaches. It serves a different architectural niche from tools like browser-use.

---

## 19. [nanochat](https://github.com/karpathy/nanochat)
> The best ChatGPT that $100 can buy.

**Language:** Python  |  **Stars:** 45,408  |  **Forks:** 6,009  |  **Score:** 2,478  |  **Created:** 2025-10-13

**Background:** Karpathy's minimal LLM training harness that covers the full stack from tokenization through pretraining, finetuning, evaluation, inference, and a chat UI. It can train a GPT-2 capability model for approximately $48 on 8xH100 GPUs (or ~$15 on spot instances) and provides a ChatGPT-like web UI for interaction.

**Problem it solves:** Training LLMs from scratch requires navigating complex distributed training setups, custom tokenizers, and evaluation frameworks. Nanochat packages the entire pipeline into a single, hackable codebase that runs on a single GPU node with a single `--depth` complexity dial.

**Why another one?** Nanochat is trending alongside autoresearch because autoresearch uses nanochat as its training substrate. The parent project's viral success is pulling nanochat back into the spotlight, reinforcing the connection between Karpathy's minimal training philosophy and autonomous AI research.

---

## 20. [text-generation-webui](https://github.com/oobabooga/text-generation-webui)
> The best local UI for large language models, with easy setup and powerful features. 100% offline.

**Language:** Python  |  **Stars:** 46,185  |  **Forks:** 5,895  |  **Score:** 2,416  |  **Created:** 2022-12-21

**Background:** Text Generation Web UI by oobabooga is a Gradio-based interface for running large language models locally, with complete offline functionality. The project has been maintained since December 2022 and has grown to over 46,000 stars as the default local LLM inference frontend.

**Problem it solves:** Running open-source LLMs locally requires dealing with model loading, quantization, sampling parameters, and API serving — tasks that are straightforward individually but tedious to set up together. Text Generation Web UI bundles all of this into a single application with a familiar chat interface.

**Why another one?** It is the incumbent local LLM UI, not a new entrant. It trends periodically as new models are released and users search for compatible inference frontends. The Deep Reason extension and continued updates keep it relevant against newer alternatives.

---

## 21. [Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana)
> Edit Banana: A framework for converting statistical formats into editable.

**Language:** Python  |  **Stars:** 2,829  |  **Forks:** 171  |  **Score:** 2,410  |  **Created:** 2026-01-16

**Background:** Edit Banana is a research framework from BIT DataLab that converts static statistical visualizations — charts, graphs, infographics — into editable assets. Powered by SAM 3 and multimodal large models, it reconstructs diagrams with high fidelity, preserving original details and logical relationships while making every element individually manipulable.

**Problem it solves:** Charts embedded in PDFs, presentations, and reports are static images that cannot be modified without recreating them from scratch. Edit Banana reverse-engineers these visualizations into editable components, allowing users to update data, change colors, or modify labels without access to the original source files.

**Why another one?** The combination of SAM 3 for element segmentation and multimodal LLMs for understanding chart semantics is technically novel. Previous chart-editing tools relied on OCR and heuristic detection, which failed on complex or stylized visualizations. Edit Banana's approach preserves logical relationships (axis scales, data series ordering), not just visual appearance.

---

## 22. [edict](https://github.com/cft0808/edict)
> Three Departments and Six Ministries - OpenClaw Multi-Agent Orchestration System with real-time dashboard, model config, and full audit trails

**Language:** Python  |  **Stars:** 5,575  |  **Forks:** 465  |  **Score:** 2,398  |  **Created:** 2026-02-23

**Background:** Edict applies the governance structure of the Tang Dynasty's Three Departments and Six Ministries system to AI multi-agent orchestration. It organizes 12 AI agents (11 specialized roles plus 1 compatibility role) into a hierarchical workflow with planning, review, approval, and execution phases, complete with a real-time dashboard and audit trails.

**Problem it solves:** Multi-agent systems like CrewAI and AutoGen lack institutional review mechanisms — any agent can take action without oversight. Edict introduces a systematic approval layer (the "Menxia" review department) that must approve plans before execution, preventing costly mistakes in automated workflows.

**Why another one?** The historical governance metaphor is more than a gimmick. The separation of planning (Zhongshu), review (Menxia), and execution (Shangshu) maps well onto real software engineering workflows where design review and approval are distinct from implementation. The real-time dashboard and full audit trails add operational visibility that most agent frameworks lack.

---

## 23. [prompts.chat](https://github.com/f/prompts.chat)
> Share, discover, and collect prompts from the community. Free and open source.

**Language:** HTML  |  **Stars:** 151,166  |  **Forks:** 19,861  |  **Score:** 2,394  |  **Created:** 2022-12-05

**Background:** Formerly "Awesome ChatGPT Prompts," prompts.chat has evolved into a full web platform for prompt sharing and discovery with community submissions, self-hosting support, and a Hugging Face dataset mirror. Over 40 academic papers have cited it as a resource.

**Problem it solves:** Crafting effective AI prompts requires trial and error. Prompts.chat provides a community-maintained library of tested prompts that serve as starting points, reducing experimentation time.

**Why another one?** It is the canonical prompt library and trends recurrently. Its evolution from a markdown file to a full platform with organizational self-hosting keeps it relevant as the prompt engineering landscape matures.

---

## 24. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster.

**Language:** Shell  |  **Stars:** 75,677  |  **Forks:** 6,100  |  **Score:** 2,365  |  **Created:** 2025-02-22

**Background:** Anthropic's first-party terminal-based coding agent continues its steady presence on trending lists. Claude Code's extensible skills and hooks system has made it a platform that other projects build upon, driving ecosystem growth that keeps the main repository visible.

**Problem it solves:** Automates repetitive development tasks, codebase navigation, and version control management directly in the terminal, eliminating context-switching between AI interfaces and development environments.

**Why another one?** Claude Code trends because it functions as platform infrastructure for the agent skills ecosystem. Multiple repositories on today's list — ECC, Superpowers, Impeccable, PM Skills — are built to extend Claude Code's capabilities.

---

## 25. [BettaFish](https://github.com/666ghj/BettaFish)
> Multi-agent public opinion analysis assistant, breaking information cocoons, restoring opinion landscapes, predicting trends, and assisting decision-making

**Language:** Python  |  **Stars:** 37,217  |  **Forks:** 7,022  |  **Score:** 2,284  |  **Created:** 2024-07-01

**Background:** BettaFish is a multi-agent public opinion and sentiment analysis assistant by the same team behind MiroFish. Built from scratch without relying on any agent framework, it uses multiple specialized agents to collect, analyze, and visualize public sentiment across media channels. The project aims to break information filter bubbles by presenting the full opinion landscape rather than algorithmically filtered views.

**Problem it solves:** Social media algorithms create information cocoons where users only see opinions that reinforce their existing views. BettaFish aggregates sentiment across sources, presents the full spectrum of opinions on a topic, and predicts how public sentiment is likely to evolve — giving users a more complete picture for decision-making.

**Why another one?** BettaFish's independence from existing agent frameworks (no CrewAI, no AutoGen) is a deliberate architectural choice that gives the team full control over agent coordination and data flow. The combination of opinion analysis, prediction, and information-bubble-breaking positions it as a civic technology tool rather than just another sentiment analyzer.

---

> **Day's theme:** Autonomous AI research enters the spotlight as Karpathy's autoresearch dominates with an explosive score, while the broader ecosystem continues building orchestration, governance, and design layers that make agent-driven workflows production-ready.
