# Trendshift Report Template

Use this template when writing the deep-dive report after fetching repo data and READMEs.

---

## Report Header

```
# Trendshift Report — {YYYY-MM-DD}
**Total:** {N} repositories

---
```

---

## Per-Repo Block

```markdown
## {rank}. [{repo-name}]({github_url})
> {one-line description from API}

**Language:** {lang}  |  **Stars:** {stars}  |  **Forks:** {forks}  |  **Score:** {score}  |  **Created:** {YYYY-MM-DD}

**Background:** 2-3 sentences on what the project is, who made it, and its history/context.

**Problem it solves:** What specific pain point does this address? Why does it exist? What was broken or missing before it?

**Why another one?** What makes this distinct from existing alternatives? What's the differentiating angle — architecture, philosophy, target user, size, license, ecosystem?

---
```

### Rules

- Heading: `## {rank}. [{repo-name}]({github_url})` — repo name only (not owner/repo), linked to GitHub
- Keep the `> description` line from the API as a one-liner quote
- Meta line: Language | Stars | Forks | Score | Created — no Trendshift link
- Three prose sections: **Background**, **Problem it solves**, **Why another one?**
- Each section is 2-4 sentences. Be specific — avoid vague marketing language
- If the repo is well-known (e.g. PostHog, claude-code), the "Why another one?" can explain why it keeps trending rather than why it was created
- Base descriptions on README content; do not hallucinate features not in the README

---

## Day Summary (end of report)

Close the report with a one-line theme:

```
> **Day's theme:** {one sentence capturing the dominant narrative across all 25 repos}
```
