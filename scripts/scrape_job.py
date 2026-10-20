#!/usr/bin/env python3
"""
Job Research Scraper using Scrapling
Fetches Job Descriptions (JDs) and company pages using Scrapling's StealthyFetcher,
sanitizes noise, and converts the content into clean Markdown suitable for AI analysis.

Usage:
    python scripts/scrape_job.py <URL> [--output <file_path>] [--save]
"""

import sys
import os
import re
import argparse
from datetime import datetime
from urllib.parse import urlparse

try:
    from scrapling import StealthyFetcher, Fetcher
    from scrapling.core.ai import Convertor
    from scrapling.parser import Selector
except ImportError as e:
    print(f"Error: Missing dependency ({e}). Run: pip install 'scrapling[all]' markdownify")
    sys.exit(1)


def sanitize_filename(name: str) -> str:
    """Sanitize string for file naming."""
    name = re.sub(r'[^\w\s-]', '', name).strip().lower()
    return re.sub(r'[-\s]+', '-', name)[:50]


def scrape_job(url: str, stealth: bool = True, timeout: int = 30000) -> dict:
    """
    Scrape a job URL using Scrapling.
    Returns a dictionary with title, markdown content, and metadata.
    """
    print(f"[*] Fetching: {url}")
    domain = urlparse(url).netloc

    # Use StealthyFetcher for anti-bot bypass on modern job boards
    try:
        if stealth:
            print("[*] Running Scrapling StealthyFetcher (headless browser + stealth)...")
            page = StealthyFetcher.fetch(
                url,
                headless=True,
                timeout=timeout,
                network_idle=True
            )
        else:
            print("[*] Running Scrapling standard Fetcher...")
            page = Fetcher.get(url, timeout=timeout // 1000)
    except Exception as err:
        print(f"[!] Primary fetch failed ({err}). Falling back to Fetcher...")
        page = Fetcher.get(url, timeout=timeout // 1000)

    if page.status not in (200, 201):
        print(f"[!] Warning: HTTP Status {page.status}")

    # Extract page title
    title_el = page.css("title::text").first
    title = str(title_el).strip() if title_el else "Job Posting"

    # Extract clean markdown using Scrapling's Convertor
    extracted = list(Convertor._extract_content(
        page,
        extraction_type="markdown",
        main_content_only=True
    ))
    markdown_body = "".join(extracted).strip()

    # If main content extraction was too aggressive or empty, extract from full page
    if len(markdown_body) < 150:
        extracted = list(Convertor._extract_content(
            page,
            extraction_type="markdown",
            main_content_only=False
        ))
        markdown_body = "".join(extracted).strip()

    return {
        "url": url,
        "domain": domain,
        "title": title,
        "status": page.status,
        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "content_markdown": markdown_body
    }


def main():
    parser = argparse.ArgumentParser(description="Scrape and extract clean Markdown from job postings.")
    parser.add_argument("url", help="Job posting or company URL to scrape")
    parser.add_argument("--save", action="store_true", help="Save directly to data/jobs/")
    parser.add_argument("--output", "-o", help="Custom output file path (.md)")
    parser.add_argument("--no-stealth", action="store_true", help="Disable stealth browser, use plain HTTP")

    args = parser.parse_args()

    data = scrape_job(args.url, stealth=not args.no_stealth)

    header = f"""---
title: "{data['title']}"
source_url: {data['url']}
scraped_at: {data['scraped_at']}
domain: {data['domain']}
---

# {data['title']}

- **Source**: [{data['domain']}]({data['url']})
- **Scraped Date**: {data['scraped_at']}

---

## 📋 Scraped Content

{data['content_markdown']}
"""

    if args.output:
        out_path = args.output
    elif args.save:
        os.makedirs("data/jobs", exist_ok=True)
        safe_title = sanitize_filename(data['title']) or "job_posting"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = f"data/jobs/{timestamp}_{safe_title}.md"
    else:
        out_path = None

    if out_path:
        os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(header)
        print(f"\n[+] Successfully saved to: {out_path}")
    else:
        print("\n" + "=" * 50)
        print(header)
        print("=" * 50)


if __name__ == "__main__":
    main()
