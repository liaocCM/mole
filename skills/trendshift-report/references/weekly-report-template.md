# Trendshift Weekly Report Template

Use this template when writing the weekly aggregated report from daily JSON caches.

---

## Report Header

```
# Trendshift Weekly Report — {start-date} to {end-date}
**Total unique repositories:** {N} (from {M} daily entries across {D} days)

---
```

---

## Per-Repo Block

```markdown
## {rank}. [{repo-name}]({github_url})
> {one-line description from API}

**Language:** {lang}  |  **Stars:** {stars}  |  **Forks:** {forks}  |  **Best Score:** {score}  |  **Best Rank:** #{rank}  |  **Days on chart:** {X}/{D}  |  **Created:** {YYYY-MM-DD}

**Background:** 2-3 sentences on what the project is, who made it, and its history/context.

**Problem it solves:** What specific pain point does this address? Why does it exist? What was broken or missing before it?

**Why another one?** What makes this distinct from existing alternatives? What's the differentiating angle — architecture, philosophy, target user, size, license, ecosystem?

---
```

### Rules

- Heading: `## {rank}. [{repo-name}]({github_url})` — repo name only (not owner/repo), linked to GitHub
- Keep the `> description` line from the API as a one-liner quote
- Meta line includes: Language | Stars | Forks | Best Score | Best Rank | Days on chart | Created
- Stars/Forks: use the highest value seen across the week
- Best Score: highest trendshift score observed during the week
- Best Rank: best (lowest number) daily rank achieved
- Days on chart: how many of the {D} days this repo appeared in the top 25
- Three prose sections: **Background**, **Problem it solves**, **Why another one?**
- Each section is 2-4 sentences. Be specific — avoid vague marketing language
- Base descriptions on README content; do not hallucinate features not in the README

---

## Week Summary (end of report)

Close the report with a one-line theme:

```
> **Week's theme:** {one sentence capturing the dominant narrative across the week's trending repos}
```
