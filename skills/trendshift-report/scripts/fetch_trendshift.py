#!/usr/bin/env python3
"""Fetch trending repositories from trendshift.io for a given date."""

import sys
import json
import argparse
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

NEXT_ACTION = "7f126a89d9d76be465096980443c804b5c83e35e18"
TRENDSHIFT_URL = "https://trendshift.io/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
README_MAX_CHARS = 4000


def fetch_trending(date: str, language: str = "all") -> list:
    payload = json.dumps([date, language]).encode()
    req = urllib.request.Request(
        TRENDSHIFT_URL,
        data=payload,
        headers={**HEADERS, "next-action": NEXT_ACTION, "Content-Type": "text/plain"},
    )
    with urllib.request.urlopen(req) as response:
        content = response.read().decode()

    # Parse Next.js server action response: "0:{...}\n1:[...]\n"
    for line in content.splitlines():
        if line.startswith("1:"):
            data = json.loads(line[2:])
            if isinstance(data, list):
                return data
    return []


def fetch_readme(full_name: str) -> str:
    """Fetch README.md from GitHub, trying main then master branch."""
    for branch in ("main", "master"):
        url = f"https://raw.githubusercontent.com/{full_name}/{branch}/README.md"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as r:
                content = r.read().decode("utf-8", errors="replace")
                return content[:README_MAX_CHARS]
        except urllib.error.HTTPError:
            continue
        except Exception:
            break
    return ""


def fetch_all_readmes(repos: list) -> dict:
    """Fetch READMEs for all repos in parallel."""
    results = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_readme, r["full_name"]): r["full_name"] for r in repos}
        total = len(futures)
        done = 0
        for future in as_completed(futures):
            name = futures[future]
            done += 1
            print(f"  [{done}/{total}] fetched readme: {name}", file=sys.stderr)
            results[name] = future.result()
    return results


def format_report(repos: list, date: str, readmes: dict = None) -> str:
    lines = [
        f"# Trendshift Report — {date}",
        f"**Total:** {len(repos)} repositories",
        "",
        "---",
        "",
    ]

    for repo in repos:
        rank = repo.get("rank", "?")
        full_name = repo.get("full_name", "")
        repo_name = full_name.split("/")[-1]
        description = repo.get("repository_description", "")
        stars = repo.get("repository_stars", 0)
        forks = repo.get("repository_forks", 0)
        lang = repo.get("repository_language", "")
        score = repo.get("score", 0)
        created_at = repo.get("repository_created_at", "")[:10]

        github_url = f"https://github.com/{full_name}"

        lines.append(f"## {rank}. [{repo_name}]({github_url})")
        if description:
            lines.append(f"> {description}")
        lines.append("")

        meta_parts = []
        if lang:
            meta_parts.append(f"**Language:** {lang}")
        meta_parts.append(f"**Stars:** {stars:,}")
        meta_parts.append(f"**Forks:** {forks:,}")
        meta_parts.append(f"**Score:** {score:,}")
        if created_at:
            meta_parts.append(f"**Created:** {created_at}")
        lines.append("  |  ".join(meta_parts))

        if readmes and full_name in readmes and readmes[full_name]:
            lines.append("")
            lines.append("<details><summary>README excerpt</summary>")
            lines.append("")
            lines.append("```")
            lines.append(readmes[full_name].strip())
            lines.append("```")
            lines.append("")
            lines.append("</details>")

        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch trendshift.io trending repos")
    parser.add_argument("date", help="Date in YYYY-MM-DD format")
    parser.add_argument("--language", default="all", help="Language filter (default: all)")
    parser.add_argument("--readme", action="store_true", help="Fetch README.md for each repo")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output raw JSON (includes readme if --readme)")
    parser.add_argument("--output", help="Output file path (default: stdout)")
    args = parser.parse_args()

    try:
        user_date = datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{args.date}'. Use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    # API returns data for the day before the requested date
    api_date = (user_date - timedelta(days=1)).strftime("%Y-%m-%d")

    try:
        repos = fetch_trending(api_date, args.language)
    except urllib.error.URLError as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

    if not repos:
        print(f"No trending data found for {args.date} (api query: {api_date})", file=sys.stderr)
        sys.exit(1)

    readmes = None
    if args.readme:
        print(f"Fetching READMEs for {len(repos)} repos...", file=sys.stderr)
        readmes = fetch_all_readmes(repos)

    if args.as_json:
        output = {"date": args.date, "api_date": api_date, "language": args.language, "repos": repos}
        if readmes:
            output["readmes"] = readmes
        result = json.dumps(output, indent=2)
    else:
        result = format_report(repos, args.date, readmes)

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
        print(f"Saved to {args.output}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
