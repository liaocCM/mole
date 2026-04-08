# Trendshift Report — 2026-03-31
**Total:** 25 repositories

---

## 1. [pretext](https://github.com/chenglou/pretext)
> Fast, accurate & comprehensive text measurement & layout

**Language:** TypeScript  |  **Stars:** 39,924  |  **Forks:** 2,122  |  **Score:** 31,097  |  **Created:** 2026-03-07

**Background:** Pretext by Cheng Lou is a pure JavaScript/TypeScript library for multiline text measurement and layout that avoids DOM measurements entirely. Launched just three weeks ago, it has already amassed nearly 40,000 stars — a remarkable trajectory that reflects deep developer frustration with browser text layout performance. It supports rendering to DOM, Canvas, SVG, and soon server-side environments.

**Problem it solves:** DOM-based text measurement (via `getBoundingClientRect` or `offsetHeight`) triggers layout reflow, one of the most expensive operations in the browser. Pretext implements its own text measurement logic using the browser's font engine as ground truth, enabling pure arithmetic layout calculations that avoid reflow entirely.

**Why another one?** Pretext's approach of precomputing text metrics once and then performing layout as pure arithmetic is fundamentally different from existing solutions that rely on DOM queries. Its support for complex scripts, bidirectional text, and multiple rendering targets (DOM, Canvas, SVG) makes it a comprehensive text layout engine rather than a simple measurement utility.

---

## 2. [VibeVoice](https://github.com/microsoft/VibeVoice)
> Open-Source Frontier Voice AI

**Language:** Python  |  **Stars:** 37,119  |  **Forks:** 4,268  |  **Score:** 14,268  |  **Created:** 2025-08-25

**Background:** VibeVoice by Microsoft is an open-source frontier voice AI system covering both text-to-speech and automatic speech recognition. With over 37,000 stars and published research papers on both TTS and ASR, it has become a leading open-source voice AI platform. Its ASR component is already being adopted by community projects like Vibing, a voice-powered input method.

**Problem it solves:** High-quality voice AI — both synthesis and recognition — has historically been locked behind proprietary APIs with per-request pricing. VibeVoice provides frontier-quality TTS and ASR models that developers can run locally, eliminating dependency on cloud services and enabling offline voice applications.

**Why another one?** VibeVoice combines both TTS and ASR in a single unified project with academic backing (published papers on OpenReview and arXiv). Microsoft's engineering resources ensure model quality that rivals commercial APIs, while the open-source license and HuggingFace distribution make it accessible to individual developers and small teams.

---

## 3. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 32,070  |  **Forks:** 2,930  |  **Score:** 13,792  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice by shanraisshan is a community-maintained guide documenting proven patterns, tips, and implementation strategies for Claude Code. Actively maintained and regularly updated (most recently for Claude Code v2.1.92 on April 6, 2026), it has grown to over 32,000 stars as the go-to practitioner reference for Claude Code workflows.

**Problem it solves:** Claude Code is powerful but has a steep learning curve — users discover effective patterns through weeks of trial and error. This repository consolidates community-learned best practices, orchestration workflows, subagent strategies, and implementation patterns into a single, continuously updated reference.

**Why another one?** Unlike official documentation that focuses on features, this repository captures the practitioner perspective — what actually works in daily use, common pitfalls, and workflow patterns that emerge from real-world usage. Its community-driven nature means it reflects diverse use cases and stays current with each release.

---

## 4. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 138,686  |  **Forks:** 11,746  |  **Score:** 11,854  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, now surpassing 138,000 stars. It enforces a disciplined spec-plan-implement-review process: the agent teases out a specification, presents it in digestible chunks, builds an implementation plan, then launches subagent-driven development with built-in review cycles.

**Problem it solves:** Coding agents left to their own devices jump straight into writing code without understanding the full problem. Superpowers enforces a structured workflow with TDD and YAGNI principles, ensuring agents work methodically through each engineering task rather than producing poorly planned implementations.

**Why another one?** Superpowers focuses on development methodology rather than tool orchestration. Its subagent-driven development model allows Claude to work autonomously for hours without drifting from the plan. At 138,000 stars, it has proven its approach at scale and continues to grow as the de facto standard for structured agent-driven development.

---

## 5. [claude-howto](https://github.com/luongnv89/claude-howto)
> A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

**Language:** Python  |  **Stars:** 20,611  |  **Forks:** 2,462  |  **Score:** 11,580  |  **Created:** 2025-11-07

**Background:** Claude How To by luongnv89 is a visual, example-driven guide to mastering Claude Code, available in English, Vietnamese, and Chinese. Now at version 2.3.0, it covers everything from basic concepts to advanced agent orchestration, hooks, skills, and MCP servers, with guided learning paths and copy-paste templates.

**Problem it solves:** Most Claude Code users install the tool, run a few prompts, and then plateau — the official docs describe features individually but do not show how to combine them effectively. Claude How To provides a structured learning path with visual tutorials that take users from beginner to advanced agent orchestration.

**Why another one?** The visual, example-driven approach sets it apart from text-heavy documentation. Its guided learning path ("Find Your Level") and "Get Started in 15 Minutes" onboarding make it accessible to newcomers, while the feature catalog and advanced agent patterns serve experienced users. Multilingual support broadens its reach beyond English-speaking developers.

---

## 6. [cli](https://github.com/larksuite/cli)
> The official Lark/Feishu CLI tool, maintained by the larksuite team — built for humans and AI Agents. Covers core business domains including Messenger, Docs, Base, Sheets, Calendar, Mail, Tasks, Meetings, and more, with 200+ commands and 19 AI Agent Skills.

**Language:** Go  |  **Stars:** 6,722  |  **Forks:** 394  |  **Score:** 8,653  |  **Created:** 2026-03-25

**Background:** Lark CLI is the official command-line tool for Lark/Feishu, maintained by the larksuite team at ByteDance. Released just six days ago, it has already gained 6,700 stars. It covers 12 business domains with 200+ commands and 20 AI Agent Skills, designed from the ground up for both human developers and AI agents.

**Problem it solves:** Interacting with Lark/Feishu services programmatically requires navigating complex REST APIs with inconsistent parameter conventions. Lark CLI provides a unified, agent-native interface with smart defaults, structured output, and concise parameters that maximize AI agent call success rates.

**Why another one?** As the official CLI from the Lark/Feishu team, it carries platform authority that third-party wrappers cannot match. The three-layer architecture — shortcuts for common tasks, API commands for platform-synced operations, and raw API for full coverage — lets both humans and agents choose the right abstraction level. The 20 built-in AI Agent Skills make it immediately usable by Claude Code, Cursor, and other agent frameworks.

---

## 7. [voice-input-src](https://github.com/yetone/voice-input-src)
> N/A

**Language:** N/A  |  **Stars:** 1,799  |  **Forks:** 190  |  **Score:** 6,450  |  **Created:** 2026-03-29

**Background:** Voice Input Src by yetone is a macOS menu-bar voice input app generated entirely from a single Claude Code prompt. Released just two days ago, the repository contains the prompt itself — a detailed specification for a Swift app that uses hold-to-record with the Fn key and injects transcribed text into any focused input field using Apple's Speech Recognition framework.

**Problem it solves:** Voice input on macOS requires switching to dictation mode, which disrupts workflow and lacks real-time feedback. This app provides a hold-to-record interface with streaming transcription and an elegant floating capsule window showing real-time waveform animation and transcription text.

**Why another one?** The project is as much a demonstration of Claude Code's capabilities as it is a voice input tool. The entire app is specified in a single prompt with precise UI requirements — capsule-shaped floating windows, real-time audio waveforms, elastic text layout — showcasing how detailed prompts can produce production-quality native apps. Multi-language support (Chinese, English, Japanese, Korean) and CJK input method handling add practical utility.

---

## 8. [coding-interview-university](https://github.com/jwasham/coding-interview-university)
> A complete computer science study plan to become a software engineer.

**Language:** N/A  |  **Stars:** 340,398  |  **Forks:** 81,887  |  **Score:** 5,504  |  **Created:** 2016-06-06

**Background:** Coding Interview University by John Washam is one of GitHub's most-starred repositories — a comprehensive computer science study plan that grew from a personal to-do list into the definitive self-study guide for software engineering interviews. After following his own plan, Washam was hired at Amazon, lending credibility to the approach.

**Problem it solves:** Preparing for technical interviews at top companies requires knowing what to study from a vast computer science curriculum. Coding Interview University provides a structured, prioritized study plan covering data structures, algorithms, system design, and more, eliminating the guesswork of self-directed preparation.

**Why another one?** With 340,000 stars and translations in over 15 languages, Coding Interview University has no real competitor at its scale. Its continued presence on trending lists — a decade after creation — reflects ongoing demand from each new generation of developers entering the job market.

---

## 9. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 26,562  |  **Forks:** 3,478  |  **Score:** 5,333  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is a self-improving AI agent with a built-in learning loop — it creates skills from experience, improves them during use, and builds a deepening model of who you are across sessions. It supports any model provider (OpenRouter, OpenAI, Nous Portal, and others) and can be reached from Telegram, Discord, Slack, WhatsApp, Signal, and CLI simultaneously.

**Problem it solves:** Most AI agents start from zero in every session, losing all context and learned patterns. Hermes Agent persists knowledge across sessions, searches its own past conversations, and nudges itself to save useful context, creating an agent that genuinely improves with use rather than resetting each time.

**Why another one?** The self-improving architecture is the core differentiator — Hermes Agent does not just store memories but actively creates and refines skills from experience. Its model-agnostic design (switch providers with a single command) and multi-platform gateway (one agent, six messaging platforms) make it uniquely portable and accessible.

---

## 10. [TaxHacker](https://github.com/vas3k/TaxHacker)
> Self-hosted AI accounting app. LLM analyzer for receipts, invoices, transactions with custom prompts and categories

**Language:** TypeScript  |  **Stars:** 4,889  |  **Forks:** 750  |  **Score:** 5,110  |  **Created:** 2025-03-10

**Background:** TaxHacker by vas3k is a self-hosted AI accounting app designed for freelancers, indie hackers, and small businesses. It uses LLMs to automatically extract data from receipts, invoices, and PDFs — product names, amounts, dates, merchants, taxes — and stores everything in a structured database with filtering, multi-project support, and import/export capabilities.

**Problem it solves:** Expense tracking for freelancers involves tedious manual data entry from receipts and invoices. TaxHacker automates extraction using AI, including custom fields with user-defined prompts, automatic currency conversion (including crypto) based on historical exchange rates, and structured categorization for tax reporting.

**Why another one?** The self-hosted approach gives users full control over their financial data — no uploading sensitive documents to third-party services. Custom AI prompts for field extraction allow users to tailor the system to their specific tax jurisdiction and accounting needs, making it more flexible than purpose-built accounting software.

---

## 11. [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)
> freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**Language:** TypeScript  |  **Stars:** 441,907  |  **Forks:** 44,140  |  **Score:** 4,454  |  **Created:** 2014-12-24

**Background:** freeCodeCamp is the most-starred repository on GitHub and the open-source codebase behind freeCodeCamp.org, a donor-supported charity that has helped over 100,000 people get their first developer job. Its full-stack web development and machine learning curriculum is completely free and self-paced, with thousands of interactive coding challenges.

**Problem it solves:** Quality programming education remains expensive and inaccessible to many. freeCodeCamp provides a complete, free curriculum from responsive web design through machine learning, with certifications that demonstrate skills to potential employers.

**Why another one?** As a 501(c)(3) charity with over 440,000 stars, freeCodeCamp operates at a scale no competitor matches. Its community-driven model — where learners become contributors — creates a self-sustaining ecosystem of education and mentorship that commercial alternatives cannot replicate.

---

## 12. [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
> Teams-first Multi-agent orchestration for Claude Code

**Language:** TypeScript  |  **Stars:** 25,610  |  **Forks:** 2,352  |  **Score:** 4,422  |  **Created:** 2026-01-09

**Background:** Oh My ClaudeCode by Yeachan Heo is a multi-agent orchestration layer for Claude Code with a zero-learning-curve philosophy — "Don't learn Claude Code. Just use OMC." Available in seven languages and with a companion project for OpenAI Codex CLI, it has grown to over 25,000 stars since its January 2026 launch.

**Problem it solves:** Setting up effective multi-agent workflows in Claude Code requires understanding subagents, skills, hooks, and workflow coordination. Oh My ClaudeCode abstracts this complexity behind a simple CLI and pre-built workflows, letting teams deploy multi-agent orchestration without deep Claude Code expertise.

**Why another one?** The teams-first focus distinguishes it from individual-developer tools. Oh My ClaudeCode provides team-level coordination patterns — shared workflows, consistent orchestration across team members, and pre-configured agent hierarchies — that individual skill packages do not address. The cross-platform support (Claude Code and Codex) avoids vendor lock-in.

---

## 13. [OpenBB](https://github.com/OpenBB-finance/OpenBB)
> Financial data platform for analysts, quants and AI agents.

**Language:** Python  |  **Stars:** 65,513  |  **Forks:** 6,491  |  **Score:** 4,388  |  **Created:** 2020-12-20

**Background:** Open Data Platform by OpenBB is an open-source toolset that helps data engineers integrate proprietary, licensed, and public financial data sources into downstream applications. Operating as a "connect once, consume everywhere" infrastructure layer, it exposes data to Python environments, OpenBB Workspace, Excel, MCP servers for AI agents, and REST APIs simultaneously.

**Problem it solves:** Financial data is fragmented across dozens of providers with inconsistent APIs, formats, and authentication methods. OpenBB consolidates these into a unified platform, allowing analysts and quants to query multiple data sources through a single interface without building custom integrations for each provider.

**Why another one?** OpenBB's pivot to serving AI agents via MCP servers positions it uniquely in the current market. While traditional financial data platforms target human analysts, OpenBB's multi-surface architecture — Python, Excel, REST, and MCP — makes it the natural data layer for both human-driven and agent-driven financial workflows.

---

## 14. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 71,854  |  **Forks:** 11,138  |  **Score:** 4,197  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski provides a growing collection of meticulously crafted AI agent personas for professional roles. Born from a Reddit thread and months of iteration, it has surged past 71,000 stars. Each agent has defined personality traits, domain expertise, communication style, workflows, and deliverable templates.

**Problem it solves:** Teams adopting AI agents need role-specific system prompts and workflow definitions for every business function — frontend development, community management, content creation, and more. Agency Agents provides these ready-made, eliminating the prompt engineering overhead of creating effective personas from scratch.

**Why another one?** The personality-driven approach — agents with names, quirks, and strong opinions — makes them entertaining and shareable, driving viral adoption beyond the typical developer audience. The breadth of covered roles positions it as an agency-in-a-box rather than just a prompt library, with production-ready workflows and success metrics for each agent.

---

## 15. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies

**Language:** TypeScript  |  **Stars:** 47,959  |  **Forks:** 7,734  |  **Score:** 3,774  |  **Created:** 2026-03-02

**Background:** Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business. Launched less than a month ago, it has already accumulated nearly 48,000 stars. The tagline positions it boldly: "If OpenClaw is an employee, Paperclip is the company" — it manages org charts, budgets, governance, goal alignment, and agent coordination.

**Problem it solves:** Individual AI agents can complete tasks, but running a business requires coordinating multiple agents across departments — engineering, design, marketing, finance — with shared goals, budgets, and accountability. Paperclip provides the management layer that turns isolated agents into a functioning organization.

**Why another one?** Paperclip operates at a higher abstraction level than agent frameworks — it manages business goals rather than pull requests. The org chart and budget systems bring corporate governance concepts to AI agent teams, and the dashboard provides visibility into agent work and costs that task-level tools do not offer.

---

## 16. [hackingtool](https://github.com/Z4nzu/hackingtool)
> ALL IN ONE Hacking Tool For Hackers

**Language:** Python  |  **Stars:** 57,819  |  **Forks:** 6,421  |  **Score:** 3,761  |  **Created:** 2020-04-11

**Background:** HackingTool by Z4nzu is an all-in-one security toolkit that aggregates 185+ tools across 20 categories for security researchers and penetration testers. Now at version 2.0.0, it supports Linux, Kali, Parrot OS, and macOS, providing a unified interface to tools spanning network scanning, exploitation, forensics, and more.

**Problem it solves:** Security professionals need dozens of specialized tools for different assessment phases, each with its own installation process and interface. HackingTool provides a single installer and menu system that organizes these tools by category, reducing setup time and providing a consistent entry point.

**Why another one?** At nearly 58,000 stars, HackingTool has become the standard security toolkit aggregator. Its v2.0.0 release with tag-based organization and quick commands modernizes the interface, while the breadth of 185+ curated tools across 20 categories makes it more comprehensive than alternatives that focus on specific security domains.

---

## 17. [sherlock](https://github.com/sherlock-project/sherlock)
> Hunt down social media accounts by username across social networks

**Language:** Python  |  **Stars:** 80,033  |  **Forks:** 9,304  |  **Score:** 3,750  |  **Created:** 2018-12-24

**Background:** Sherlock is an OSINT (Open Source Intelligence) tool that hunts down social media accounts by username across hundreds of social networks. With 80,000 stars, it is one of the most popular security and investigation tools on GitHub, maintained by a dedicated project team since its 2018 launch.

**Problem it solves:** Investigating a person's online presence requires manually checking hundreds of social networks one by one. Sherlock automates this by querying all supported platforms simultaneously, quickly building a comprehensive profile of where a given username is registered.

**Why another one?** Sherlock's longevity (seven years of active maintenance) means its platform coverage is unmatched — community contributors continuously add new social networks and fix broken detections. Its simple command-line interface and no-dependency approach make it accessible to investigators who are not necessarily programmers.

---

## 18. [claude-mem](https://github.com/thedotmack/claude-mem)
> A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**Language:** TypeScript  |  **Stars:** 45,965  |  **Forks:** 3,508  |  **Score:** 3,418  |  **Created:** 2025-08-31

**Background:** Claude-Mem by thedotmack is a Claude Code plugin that automatically captures session activity, compresses it with AI using Claude's agent SDK, and injects relevant context back into future sessions. With nearly 46,000 stars and translations in over 20 languages, it has become the leading memory solution for Claude Code users.

**Problem it solves:** Claude Code sessions start with a blank slate — previous decisions, coding patterns, and project context are lost between sessions. Claude-Mem captures everything Claude does during coding sessions and resurfaces relevant memories in future sessions, creating continuity across development workflows.

**Why another one?** Claude-Mem's automatic capture and AI-powered compression distinguish it from manual context-management approaches. Rather than requiring developers to explicitly save notes, it passively records session activity and uses Claude's own agent SDK to compress and retrieve relevant context, making memory management invisible to the user.

---

## 19. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> List of Computer Science courses with video lectures.

**Language:** N/A  |  **Stars:** 79,585  |  **Forks:** 10,945  |  **Score:** 3,398  |  **Created:** 2016-10-21

**Background:** CS Video Courses by Developer-Y is a curated directory of computer science courses with video lectures, organized by topic from introductory CS through advanced machine learning, security, and quantum computing. At nearly 80,000 stars, it serves as a comprehensive index to freely available university-level CS education.

**Problem it solves:** High-quality CS video lectures exist across dozens of university websites, YouTube channels, and MOOCs, but discovering them requires extensive searching. This repository consolidates actual university-level courses (not basic tutorials) into a single, topic-organized directory.

**Why another one?** The strict curation policy — only actual college/university-level courses, no basic tutorials or advertisements — ensures quality that broader aggregators sacrifice. Nine years of community contributions have built a depth of coverage across niche CS topics (real-time systems, quantum computing, computational geometry) that newer lists have not matched.

---

## 20. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> Master programming by recreating your favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 486,645  |  **Forks:** 45,791  |  **Score:** 2,999  |  **Created:** 2018-05-09

**Background:** Build Your Own X by CodeCrafters is a compilation of step-by-step guides for recreating favorite technologies from scratch — databases, operating systems, compilers, neural networks, and more. With nearly 487,000 stars, it is among the most-starred repositories on all of GitHub, embodying Feynman's principle: "What I cannot create, I do not understand."

**Problem it solves:** Understanding how complex technologies work internally is difficult when you only use them as black boxes. Build Your Own X provides curated, well-written tutorials that walk through building these technologies from scratch, turning abstract knowledge into hands-on understanding.

**Why another one?** At 487,000 stars, this repository has no meaningful competitor. Its breadth — covering 30+ technology categories from 3D renderers to web servers — and its strict curation of well-written, step-by-step guides create a resource that individual tutorials or course platforms cannot replicate.

---

## 21. [firecrawl](https://github.com/firecrawl/firecrawl)
> The Web Data API for AI - Power AI agents with clean web data

**Language:** TypeScript  |  **Stars:** 105,249  |  **Forks:** 6,862  |  **Score:** 2,860  |  **Created:** 2024-04-15

**Background:** Firecrawl is the web data API for AI, providing search, scraping, and web interaction capabilities at scale. With over 105,000 stars, it has established itself as the industry-leading solution for powering AI agents with clean web data, offering 96% reliability across the web and available both as open source and a hosted service.

**Problem it solves:** AI agents need clean, structured data from the web, but modern websites are complex — JavaScript rendering, anti-bot measures, and inconsistent HTML make reliable scraping difficult. Firecrawl handles these complexities, delivering clean, structured data that agents can consume directly.

**Why another one?** Firecrawl's industry-leading 96% reliability rate sets it apart from alternatives that struggle with JavaScript-heavy sites. Its dual availability as open source and hosted service lets teams choose between self-hosting for control and managed service for convenience, while SDK support across multiple languages simplifies integration.

---

## 22. [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
> real time face swap and one-click video deepfake with only a single image

**Language:** Python  |  **Stars:** 89,167  |  **Forks:** 12,954  |  **Score:** 2,844  |  **Created:** 2023-09-24

**Background:** Deep-Live-Cam 2.1 is a real-time face swap and video deepfake tool that requires only a single source image. With nearly 90,000 stars, it is one of the most popular AI media tools on GitHub. The project includes built-in ethical safeguards — content checks prevent processing inappropriate media, and users must agree to responsible use terms.

**Problem it solves:** Face swapping and deepfake creation traditionally required extensive technical setup, multiple source images, and lengthy processing times. Deep-Live-Cam reduces this to a single click with a single image, enabling real-time face swapping for content creation, character animation, and fashion design.

**Why another one?** The real-time capability is the key differentiator — most deepfake tools process video offline, while Deep-Live-Cam operates in real time. The built-in ethical safeguards (content filtering, usage agreements) demonstrate responsible development practices that many competing tools lack, and the one-click simplicity removes technical barriers.

---

## 23. [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering)
> Awesome tools & guides for harness engineering.

**Language:** N/A  |  **Stars:** 1,301  |  **Forks:** 84  |  **Score:** 2,764  |  **Created:** 2026-03-29

**Background:** Awesome Harness Engineering by WalkingLabs is a curated list of articles, playbooks, benchmarks, specifications, and open-source projects for harness engineering — the emerging practice of shaping the environment around AI agents so they can work reliably. Released just two days ago, it has already gathered 1,300 stars, signaling strong interest in this nascent discipline.

**Problem it solves:** As AI agents take on longer-running and more complex tasks, the environment they operate in — context management, evaluation, observability, safe autonomy — becomes critical to reliability. This list consolidates scattered resources into a structured reference for practitioners building agent harnesses.

**Why another one?** Harness engineering is a newly defined discipline sitting at the intersection of context engineering, evaluation, orchestration, and software architecture. This is the first curated list to formalize the field, drawing from OpenAI's Codex practices, academic research, and practitioner experience to define what reliable agent infrastructure looks like.

---

## 24. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
> Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit.

**Language:** Python  |  **Stars:** 74,982  |  **Forks:** 10,187  |  **Score:** 2,718  |  **Created:** 2020-05-08

**Background:** PaddleOCR by PaddlePaddle (Baidu) is the global leading OCR toolkit and document AI engine, supporting 8 languages in its documentation and used by over 6,000 repositories. It provides a comprehensive pipeline from text detection through recognition, supporting 80+ languages and running on CPU, GPU, XPU, and NPU hardware.

**Problem it solves:** Extracting text from images and PDFs requires handling diverse languages, fonts, layouts, and document formats. PaddleOCR provides a production-ready pipeline that handles this complexity — from detecting text regions to recognizing characters across 80+ languages — without requiring deep OCR expertise.

**Why another one?** PaddleOCR's multi-hardware support (CPU, GPU, XPU, NPU) and Python 3.8-3.12 compatibility make it deployable across virtually any environment. Its five-year development history and Baidu's backing provide stability that newer OCR projects lack, while the 80+ language support covers use cases that English-focused alternatives miss.

---

## 25. [pi-mono](https://github.com/badlogic/pi-mono)
> AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack & Discord bots.

**Language:** TypeScript  |  **Stars:** 32,635  |  **Forks:** 3,567  |  **Score:** 2,675  |  **Created:** 2025-08-09

**Background:** Pi Mono by Mario Zechner (badlogic) is a monorepo containing tools for building AI agents and managing LLM deployments. The centerpiece is a coding agent CLI, accompanied by a unified LLM API, TUI and web UI libraries, and Slack/Discord bot integrations. Zechner's call for developers to share public OSS coding agent sessions reflects his commitment to improving agents through real-world data.

**Problem it solves:** Building AI agent applications requires assembling separate libraries for LLM access, UI rendering, bot integration, and coding automation. Pi Mono provides all of these in a single, well-integrated monorepo — from the LLM API layer through to user-facing interfaces and messaging platform bots.

**Why another one?** The monorepo approach ensures tight integration between components that are typically separate projects. Pi Mono's emphasis on real-world session sharing — encouraging developers to publish their agent sessions for collective improvement — creates a feedback loop that synthetic benchmarks cannot replicate. The multi-surface output (CLI, TUI, web, Slack, Discord) makes it adaptable to any team's communication preferences.

---

> **Day's theme:** The Claude Code ecosystem reaches escape velocity as practitioner guides, memory plugins, multi-agent orchestrators, and harness engineering resources dominate the chart alongside text infrastructure breakthroughs and perennial CS education staples — signaling a market that has moved from exploring what agents can do to systematically engineering the environments, workflows, and methodologies that make them reliable at scale.
