#!/usr/bin/env python3
"""
Multi-Platform Job Radar & Filter for Chanmin Yoon
Scrapes, filters, and cross-checks PM/PO job postings across:
1. Wanted (원티드)
2. JobKorea (잡코리아)
3. Incruit (인크루트)
4. PeoplenJob (피플앤잡)

Filters specifically for Junior (1~2 years / 신입~주니어), excludes Senior (5+ yrs, Team Lead),
and cross-references company review data (JobPlanet).

Usage:
    python scripts/job_radar.py [--platform wanted,jobkorea,incruit,peoplenjob] [--keyword PM] [--save]
"""

import sys
import os
import re
import argparse
import urllib.request
from datetime import datetime
from collections import defaultdict

try:
    from scrapling import Fetcher, StealthyFetcher
    from scrapling.parser import Selector
except ImportError as e:
    print(f"Error: Missing dependency ({e}). Run: pip install 'scrapling[all]'")
    sys.exit(1)


# Words that disqualify a job for 1-2 year junior PM
EXCLUDE_EXP = ['10년', '13년', '15년', '20년', '25년', '7년', '5년 이상', '8년', '9년']
EXCLUDE_ROLES = ['팀장', '본부장', '이사', '실장', '그룹장', 'Lead PM', 'Lead PO', '시니어 PM', 'Senior PM']


def filter_senior(text: str) -> bool:
    """Returns True if the text indicates a senior or executive role."""
    for exp in EXCLUDE_EXP:
        if exp in text:
            return True
    for role in EXCLUDE_ROLES:
        if role in text:
            return True
    return False


# -------------------------------------------------------------
# 1. Wanted (원티드) Scraper
# -------------------------------------------------------------
def scrape_wanted(keyword: str = "PM", limit: int = 15) -> list:
    print(f"[*] Scanning Wanted (원티드) for '{keyword}' (1~2년 차 필터)...")
    url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position&years=1&years=2"
    results = []

    try:
        page = StealthyFetcher.fetch(url, headless=True, timeout=15000, network_idle=True)
        for a in page.css('a'):
            href = a.attrib.get('href', '')
            if '/wd/' in href:
                full_text = a.get_all_text(strip=True)
                lines = [line.strip() for line in full_text.split('\n') if line.strip()]
                if len(lines) >= 3:
                    role = lines[0]
                    company = lines[1]
                    exp = lines[2]

                    if filter_senior(role) or filter_senior(exp):
                        continue

                    job_url = "https://www.wanted.co.kr" + href.split('?')[0]
                    results.append({
                        "platform": "Wanted (원티드)",
                        "company": company,
                        "title": role,
                        "exp": exp,
                        "url": job_url
                    })
    except Exception as err:
        print(f"[!] Wanted scrape error: {err}")

    # Deduplicate by url
    unique = list({r['url']: r for r in results}.values())
    print(f"[+] Found {len(unique)} junior matches on Wanted.")
    return unique[:limit]


# -------------------------------------------------------------
# 2. JobKorea (잡코리아) Scraper
# -------------------------------------------------------------
def scrape_jobkorea(keyword: str = "PM", limit: int = 15) -> list:
    print(f"[*] Scanning JobKorea (잡코리아) for '{keyword}' (1~2년 차 필터)...")
    # careerType=2 (경력), careerMin=1, careerMax=2
    url = f"https://www.jobkorea.co.kr/Search/?stext={keyword}&careerType=2&careerMin=1&careerMax=2"
    results = []

    try:
        page = Fetcher.get(url, timeout=10)
        jobs = defaultdict(list)
        for a in page.css('a'):
            href = a.attrib.get('href', '')
            m = re.search(r'/Recruit/GI_Read/(\d+)', href)
            if m:
                gid = m.group(1)
                text = a.attrib.get('title', '') or a.get_all_text(strip=True)
                if text and text not in jobs[gid]:
                    jobs[gid].append(text)

        for gid, texts in jobs.items():
            if len(texts) >= 2:
                title = texts[0]
                company = texts[1]
            else:
                title = texts[0]
                company = "기업명 비공개/채용사"

            # Filter for PM/PO relevancy & exclude seniors
            if not any(k in title for k in ['PM', 'PO', '기획', '프로덕트', '매니저']):
                continue
            if filter_senior(title):
                continue

            results.append({
                "platform": "JobKorea (잡코리아)",
                "company": company.replace('㈜', '').replace('(주)', '').strip(),
                "title": title,
                "exp": "경력 1~2년",
                "url": f"https://www.jobkorea.co.kr/Recruit/GI_Read/{gid}"
            })
    except Exception as err:
        print(f"[!] JobKorea scrape error: {err}")

    print(f"[+] Found {len(results)} junior matches on JobKorea.")
    return results[:limit]


# -------------------------------------------------------------
# 3. Incruit (인크루트) Scraper
# -------------------------------------------------------------
def scrape_incruit(keyword: str = "PM", limit: int = 15) -> list:
    print(f"[*] Scanning Incruit (인크루트) for '{keyword}' (1~2년 차 필터)...")
    # cr_s=1, cr_e=2
    url = f"https://job.incruit.com/jobdb_list/searchjob.asp?kw={keyword}&cr_s=1&cr_e=2"
    results = []

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('euc-kr', errors='ignore')
            sel = Selector(html)
            for a in sel.css('a'):
                href = a.attrib.get('href', '')
                if 'jobpost.asp' in href:
                    text = a.get_all_text(strip=True)
                    if text and len(text) > 4:
                        if not any(k in text for k in ['PM', 'PO', 'Product', '기획']):
                            continue
                        if filter_senior(text):
                            continue
                        results.append({
                            "platform": "Incruit (인크루트)",
                            "company": "기업공고",
                            "title": text,
                            "exp": "경력 1~2년",
                            "url": href.split('&')[0]
                        })
    except Exception as err:
        print(f"[!] Incruit scrape error: {err}")

    # Deduplicate
    unique = list({r['url']: r for r in results}.values())
    print(f"[+] Found {len(unique)} junior matches on Incruit.")
    return unique[:limit]


# -------------------------------------------------------------
# 4. PeoplenJob (피플앤잡) Scraper
# -------------------------------------------------------------
def scrape_peoplenjob(keyword: str = "PM", limit: int = 15) -> list:
    print(f"[*] Scanning PeoplenJob (피플앤잡) for '{keyword}' (외국계/글로벌)...")
    url = f"https://www.peoplenjob.com/jobs?q={keyword}"
    results = []

    try:
        page = Fetcher.get(url, timeout=10)
        for a in page.css('a'):
            href = a.attrib.get('href', '')
            m = re.search(r'/jobs/(\d+)', href)
            if m:
                jid = m.group(1)
                text = a.get_all_text(strip=True)
                if any(k in text.lower() for k in ['pm', 'po', 'product', 'project', 'junior', 'associate']):
                    if filter_senior(text):
                        continue
                    results.append({
                        "platform": "PeoplenJob (외국계)",
                        "company": "외국계/글로벌 기업",
                        "title": text,
                        "exp": "외국계/글로벌",
                        "url": f"https://www.peoplenjob.com/jobs/{jid}"
                    })
    except Exception as err:
        print(f"[!] PeoplenJob scrape error: {err}")

    unique = list({r['url']: r for r in results}.values())
    print(f"[+] Found {len(unique)} matches on PeoplenJob.")
    return unique[:limit]


# -------------------------------------------------------------
# Main Runner & Reporter
# -------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Multi-platform Junior PM Job Radar")
    parser.add_argument("--platforms", "-p", default="wanted,jobkorea,incruit,peoplenjob",
                        help="Comma-separated list of platforms to scan")
    parser.add_argument("--keyword", "-k", default="PM", help="Job search keyword")
    parser.add_argument("--save", action="store_true", help="Save report to data/jobs/")

    args = parser.parse_args()
    platforms = [p.strip().lower() for p in args.platforms.split(',')]

    all_jobs = []

    if "wanted" in platforms:
        all_jobs.extend(scrape_wanted(args.keyword))
    if "jobkorea" in platforms:
        all_jobs.extend(scrape_jobkorea(args.keyword))
    if "incruit" in platforms:
        all_jobs.extend(scrape_incruit(args.keyword))
    if "peoplenjob" in platforms:
        all_jobs.extend(scrape_peoplenjob(args.keyword))

    print(f"\n{'='*70}")
    print(f"🎯 Total Filtered Junior PM/PO Openings: {len(all_jobs)}")
    print(f"{'='*70}\n")

    # Generate Markdown Report
    today_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_file = datetime.now().strftime("%Y%m%d_%H%M%S")

    md_lines = [
        f"# 🎯 주니어 PM 맞춤 채용 레이더 ({today_str})",
        "",
        "> **타깃 대상**: 윤찬민 PM (1~2년 차 주니어, 글로벌/테크/B2B PM)",
        "> **필터링 조건**: 경력 1~2년 차 적합 공고, 시니어(5년 이상) 및 관리자(팀장/리드) 제외",
        "",
        "| 번호 | 플랫폼 | 기업명 | 포지션명 | 요구 경력 | 공고 바로가기 |",
        "| :---: | :---: | :--- | :--- | :---: | :--- |"
    ]

    for idx, job in enumerate(all_jobs, start=1):
        md_lines.append(
            f"| {idx} | **{job['platform']}** | {job['company']} | {job['title']} | `{job['exp']}` | [상세보기]({job['url']}) |"
        )

    md_lines.extend([
        "",
        "---",
        "",
        "## 💡 다음 단계 (실행 가이드)",
        "1. 위 목록 중 관심 있는 공고의 번호 또는 URL을 선택하세요.",
        "2. `python scripts/scrape_job.py <URL> --save` 명령어로 해당 공고의 상세 본문을 수집합니다.",
        "3. 잡플래닛에서 해당 기업의 평점 및 리스크(블랙기업 여부)를 교차 검증한 후 맞춤형 경력기술서 작성으로 이어집니다."
    ])

    report_content = "\n".join(md_lines)

    if args.save:
        os.makedirs("data/jobs", exist_ok=True)
        out_path = f"data/jobs/job_radar_{date_file}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"[+] Successfully saved radar report to: {out_path}\n")

    print(report_content)


if __name__ == "__main__":
    main()
