import { test, expect } from "@playwright/test";

test.describe("Quartz Tech Notes Blog E2E Tests", () => {
  test("1. Homepage loads properly with title, header and core UI", async ({ page }) => {
    const response = await page.goto("");
    expect(response?.status()).toBe(200);

    // Verify Title & Brand
    await expect(page).toHaveTitle(/Chanmin's Tech Archive/i);
    const mainHeading = page.locator("h1.article-title");
    await expect(mainHeading).toContainText("Chanmin's Tech Archive");

    // Verify Core UI controls are present
    await expect(page.locator(".darkmode")).toBeVisible();
  });

  test("2. Navigates to AI & Agent Engineering note and verifies content", async ({ page }) => {
    const response = await page.goto("ai/");
    expect(response?.status()).toBe(200);

    // Verify title and content
    await expect(page.locator("h1.article-title")).toContainText("AI & Agents");
    const content = page.locator("article");
    await expect(content).toContainText("에이전트 아키텍처");
  });

  test("3. Navigates to Tools hub and verifies tool matrix", async ({ page }) => {
    const response = await page.goto("tools/");
    expect(response?.status()).toBe(200);

    await expect(page.locator("h1.article-title")).toContainText("Tools");
    const content = page.locator("article");
    await expect(content).toContainText("Claude Code");
    await expect(content).toContainText("Cursor");
    await expect(content).toContainText("OpenRouter");
    await expect(content).toContainText("Langfuse");
  });

  test("4. Navigates to References and verifies structure", async ({ page }) => {
    const response = await page.goto("references/");
    expect(response?.status()).toBe(200);

    await expect(page.locator("h1.article-title")).toContainText("References");
    const article = page.locator("article");
    await expect(article).toContainText("B2B SaaS UX");
  });

  test("5. Dark mode toggle switches themes", async ({ page }) => {
    await page.goto("");

    const darkmodeBtn = page.locator(".darkmode").first();
    await expect(darkmodeBtn).toBeVisible();

    const initialTheme = await page.evaluate(() =>
      document.documentElement.getAttribute("saved-theme")
    );

    await darkmodeBtn.click();
    await page.waitForTimeout(300);

    const toggledTheme = await page.evaluate(() =>
      document.documentElement.getAttribute("saved-theme")
    );

    expect(toggledTheme).not.toBe(initialTheme);
  });

  test("6. Search modal opens when clicking search trigger", async ({ page }) => {
    await page.goto("");

    const searchBtn = page.locator(".search-button").first();
    await expect(searchBtn).toBeVisible();
    await searchBtn.click();

    // Verify search container is active and search input is visible
    const searchContainer = page.locator(".search-container.active, .search-container");
    const searchInput = page.locator("input.search-bar");
    await expect(searchContainer).toBeVisible({ timeout: 5000 });
    await expect(searchInput).toBeVisible({ timeout: 5000 });

    // Type a query and verify results display
    await searchInput.fill("AI");
    await page.waitForTimeout(500);
    const searchLayout = page.locator(".search-layout");
    await expect(searchLayout).toBeVisible({ timeout: 5000 });
  });

  test("7. Crawls and verifies all internal links return HTTP 200", async ({ page, request }) => {
    await page.goto("");

    // Extract all internal links on the page
    const links = await page.$$eval("a[href]", (elements) =>
      elements
        .map((el) => el.getAttribute("href"))
        .filter(
          (href): href is string =>
            !!href &&
            !href.startsWith("http://") &&
            !href.startsWith("https://") &&
            !href.startsWith("mailto:") &&
            !href.startsWith("tel:") &&
            !href.startsWith("javascript:") &&
            !href.startsWith("#")
        )
    );

    const uniqueLinks = Array.from(new Set(links));
    expect(uniqueLinks.length).toBeGreaterThan(0);

    for (const link of uniqueLinks) {
      const fullUrl = new URL(link, page.url()).href;
      const res = await request.get(fullUrl);
      expect(res.status(), `Broken link found: ${fullUrl}`).toBe(200);
    }
  });

  test("8. Page view counter badge is rendered in content-meta", async ({ page }) => {
    await page.goto("ai/");
    const viewCounter = page.locator(".content-meta .view-counter img.view-counter-img");
    await expect(viewCounter).toBeVisible({ timeout: 10000 });
    await expect(viewCounter).toHaveAttribute("alt", "조회수");
    await expect(viewCounter).toHaveAttribute("src", /hits\.sh\/l-yoon\.github\.io\/archive\/ai/);
  });

  test("9. Newly added tool pages load properly with valid headings and content", async ({ page }) => {
    const pages = [
      { path: "tools/google-ai-edge-foresight", title: /Google AI Edge Foresight/ },
      { path: "tools/rea", title: /REA/ },
      { path: "tools/openbot", title: /OpenBot/ },
      { path: "tools/anarlog", title: /Anarlog/ },
      { path: "tools/aside", title: /Aside/ },
      { path: "tools/claude-code-and-plugins", title: /Claude Code/ },
      { path: "tools/claude-duet", title: /Claude Duet/ },
      { path: "references/test-pyramid-strategy", title: /테스트 피라미드는 왜 여전히 유효한가/ },
      { path: "references/state-diagram", title: /상태 다이어그램/ },
    ];

    for (const item of pages) {
      const response = await page.goto(item.path);
      expect(response?.status()).toBe(200);
      await expect(page.locator("h1.article-title")).toHaveText(item.title);
      await expect(page.locator("article")).toBeVisible();
      // Ensure no raw mermaid errors or syntax crash
      await expect(page.locator(".mermaid[data-processed='false']")).toHaveCount(0);
    }
  });

  test("10. Folder counts are rendered next to category titles in Explorer", async ({ page }) => {
    await page.goto("");

    // If on mobile, open the explorer drawer
    const mobileToggle = page.locator(".explorer-toggle.mobile-explorer");
    if (await mobileToggle.isVisible()) {
      await mobileToggle.click();
    }

    const folderContainers = page.locator(".explorer .folder-container");
    await expect(folderContainers.first()).toBeVisible({ timeout: 10000 });

    const folderCounts = page.locator(".explorer .folder-container .folder-count");
    await expect(folderCounts.first()).toBeVisible({ timeout: 10000 });

    const countTexts = await folderContainers.allInnerTexts();
    expect(countTexts.some((t) => /\(\d+\)/.test(t))).toBe(true);
  });
});
