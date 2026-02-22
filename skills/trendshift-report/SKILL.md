---
name: trendshift-report
description: Fetch trending open-source repositories from trendshift.io for a specific date and generate a formatted markdown summary report with GitHub links. Use when the user asks for a trendshift report, trendshift trending repos, trending GitHub projects by date, or wants a summary of what was trending on a specific date.
---

# Trendshift Report

Fetch and format trending repositories from trendshift.io by date using the bundled script.

## Usage

```bash
# Basic report
python3 scripts/fetch_trendshift.py 2026-02-22

# With README data for deep descriptions (recommended for rich reports)
python3 scripts/fetch_trendshift.py 2026-02-22 --readme --json > /tmp/trendshift.json

# With language filter
python3 scripts/fetch_trendshift.py 2026-02-22 --language Python

# Save to file
python3 scripts/fetch_trendshift.py 2026-02-22 --output report-2026-02-22.md
```

## Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `date` | Date in YYYY-MM-DD format (required) | `2026-02-22` |
| `--language` | Language filter (default: `all`) | `Python`, `TypeScript`, `Go`, `Rust` |
| `--readme` | Fetch README.md for each repo (parallel) | |
| `--json` | Output raw JSON instead of markdown | |
| `--output` | Save report to file instead of stdout | `report.md` |

## Date Offset

The API returns data for the day *before* the date in the query. The script handles this automatically: pass the date the user requested, and the script subtracts 1 day before calling the API. The report header shows the user's requested date.

## Deduplication

Before generating any report, check if `skills/trendshift-report/data/trendshift-{date}.md` already exists. If it does, notify the user and skip generation unless they explicitly ask to regenerate.

## Output Location

Always save reports to `skills/trendshift-report/data/trendshift-{date}.md`. After writing the file, briefly confirm completion — do **not** print the full report content in the terminal.

## Workflow

**Quick report** (no READMEs):
1. Run `scripts/fetch_trendshift.py {date}`
2. Save output to `skills/trendshift-report/data/trendshift-{date}.md`
3. Confirm with a one-line summary (e.g. "Saved trendshift-2026-02-20.md — 25 repos")

**Deep report** (with README-based descriptions):
1. Run `scripts/fetch_trendshift.py {date} --readme --json > /tmp/trendshift.json`
2. Read the JSON to get repo data + README excerpts
3. Write the report to `skills/trendshift-report/data/trendshift-{date}.md` following `references/report-template.md`
4. Confirm with a one-line summary — do not print the full report

## Report Format

See `references/report-template.md` for the exact format — load it when writing a deep report.

## Notes

- If the request returns a 403 error, the `next-action` header hash may be outdated — update `NEXT_ACTION` in `scripts/fetch_trendshift.py`
- Data may be unavailable for today/yesterday; trendshift.io updates daily
- Language names are case-sensitive (e.g., `Python`, `TypeScript`, `Go`, `Rust`, `C++`)
