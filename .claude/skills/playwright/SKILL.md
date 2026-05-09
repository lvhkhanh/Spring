---
name: playwright
description: '**WORKFLOW SKILL** — Create, maintain, debug, and run Playwright browser automation and end-to-end tests. USE FOR: Playwright test suites, browser automation scripts, locators, fixtures, page objects, visual checks, trace debugging, CI browser setup, and flaky UI test investigation. DO NOT USE FOR: non-browser unit tests, Cypress-only work, Selenium-only work, or manual QA plans without automation. INVOKES: file system tools for test and config files, terminal for Playwright commands, browser tooling for screenshots and traces, semantic search for existing test patterns.'
---

# Playwright Skill

## Overview

This skill provides focused support for Playwright-based browser testing and automation. It covers project setup, test authoring, reliable selectors, fixtures, network mocking, screenshots, traces, CI execution, and debugging flaky user-interface behavior.

## Key Capabilities

### Project Setup
- Create and update `playwright.config.ts` or `playwright.config.js`
- Configure browsers, projects, base URLs, retries, workers, timeouts, and reporters
- Add test scripts and browser installation commands
- Align Playwright setup with the repository's existing package manager and test conventions

### Test Authoring
- Write end-to-end tests for critical user journeys
- Use robust locators based on roles, labels, text, test IDs, and accessible names
- Add assertions for visible UI state, navigation, requests, downloads, dialogs, and storage
- Keep tests independent, deterministic, and readable

### Fixtures and Reuse
- Create fixtures for authentication, test data, API clients, and browser contexts
- Use setup projects for login state when appropriate
- Build page objects or helper functions only when they remove real duplication
- Keep reusable helpers explicit enough that test intent remains visible

### Debugging and Diagnostics
- Use traces, screenshots, videos, console logs, and network logs to diagnose failures
- Run headed, debug, and UI modes for interactive investigation
- Identify timing, selector, environment, and data isolation causes of flakiness
- Capture minimal reproduction steps before changing tests or application code

### CI and Reporting
- Configure Playwright in GitHub Actions, Azure DevOps, Jenkins, or similar pipelines
- Install browsers and dependencies consistently in CI
- Upload HTML reports, traces, screenshots, and videos as artifacts
- Tune retries and parallelism without hiding real instability

## Usage Examples

### Add End-to-End Test
```
Create a Playwright test for the checkout flow.
Cover login, adding an item to the cart, payment validation,
and successful order confirmation.
```

### Debug Flaky Test
```
This Playwright test fails only in CI.
Inspect the test, selectors, waits, and trace output,
then propose the smallest reliable fix.
```

### Configure Playwright
```
Add Playwright config for Chromium, Firefox, and WebKit,
with HTML reports, retries in CI, and a dev server command.
```

### Add Auth Fixture
```
Create a reusable authenticated page fixture
that logs in once and saves storage state for later tests.
```

## Common Patterns

### Basic Test
```ts
import { test, expect } from '@playwright/test';

test('user can view account settings', async ({ page }) => {
  await page.goto('/settings');

  await expect(page.getByRole('heading', { name: 'Settings' })).toBeVisible();
  await expect(page.getByLabel('Email')).toHaveValue(/@/);
});
```

### Robust Locators
```ts
await page.getByRole('button', { name: 'Save' }).click();
await page.getByLabel('Email address').fill('user@example.com');
await page.getByTestId('order-status').getByText('Paid').waitFor();
```

### Waiting for Network and UI
```ts
const responsePromise = page.waitForResponse(
  response => response.url().includes('/api/orders') && response.status() === 201
);

await page.getByRole('button', { name: 'Place order' }).click();

const response = await responsePromise;
await expect(page.getByText('Order confirmed')).toBeVisible();
expect(await response.json()).toMatchObject({ status: 'confirmed' });
```

### Auth Storage State
```ts
import { test as setup, expect } from '@playwright/test';

setup('authenticate', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill(process.env.TEST_USER_EMAIL!);
  await page.getByLabel('Password').fill(process.env.TEST_USER_PASSWORD!);
  await page.getByRole('button', { name: 'Sign in' }).click();

  await expect(page.getByRole('button', { name: 'Account' })).toBeVisible();
  await page.context().storageState({ path: 'playwright/.auth/user.json' });
});
```

### Playwright Config Baseline
```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: [['html'], ['list']],
  use: {
    baseURL: process.env.BASE_URL ?? 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
  ],
});
```

### Useful Commands
```bash
npx playwright test
npx playwright test tests/e2e/login.spec.ts
npx playwright test --headed
npx playwright test --debug
npx playwright test --ui
npx playwright show-report
npx playwright show-trace trace.zip
```

## Best Practices

### Selectors
- Prefer role, label, placeholder, text, and test ID locators over CSS or XPath
- Assert accessible names for important controls
- Use `data-testid` for elements that lack stable user-facing semantics
- Avoid selectors tied to styling, DOM depth, or generated class names

### Test Reliability
- Let Playwright auto-wait through locators and assertions
- Avoid fixed sleeps such as `waitForTimeout` unless debugging temporarily
- Keep each test independent and reset state through API, fixtures, or isolated test data
- Control time, randomness, network responses, and environment-specific data where needed

### Test Design
- Cover high-value user journeys with end-to-end tests
- Move pure business logic checks to lower-level tests
- Keep setup short and visible in each scenario
- Use page objects sparingly and avoid hiding assertions inside generic actions

### CI
- Run `npx playwright install --with-deps` or the equivalent image setup in CI
- Upload Playwright reports and failure artifacts
- Use retries as diagnostics, not as a substitute for fixing flaky tests
- Keep browser matrix practical for the risk and runtime budget

## Troubleshooting

### Test Times Out
- Confirm the app server is running and `baseURL` is correct
- Replace manual waits with locator assertions or network waits
- Check whether the selector matches multiple elements or no elements
- Inspect trace viewer for the last successful action

### Test Passes Locally but Fails in CI
- Compare viewport, browser, environment variables, locale, timezone, and permissions
- Check slower CI timing and missing browser dependencies
- Verify test data isolation and parallel worker conflicts
- Review screenshots, videos, and traces from CI artifacts

### Locator Is Brittle
- Switch to `getByRole`, `getByLabel`, or `getByTestId`
- Add accessible names or stable test IDs in application code when appropriate
- Avoid relying on nth-child, CSS class names, or animation timing

### Authentication Is Unstable
- Use storage state setup for shared login when it improves speed and reliability
- Regenerate storage state when auth cookies expire
- Keep test credentials in environment variables or CI secrets
- Avoid sharing mutable user accounts across parallel tests

## Integration Points

- **Test frameworks**: `@playwright/test`, Jest/Vitest-adjacent projects, API tests
- **Frontend stacks**: React, Vue, Angular, Next.js, Remix, static sites
- **CI/CD**: GitHub Actions, Azure DevOps, GitLab CI, Jenkins
- **Diagnostics**: trace viewer, HTML report, screenshots, videos, console and network logs
- **Quality workflows**: smoke tests, regression suites, visual checks, accessibility checks
- **Browser automation**: scraping, screenshots, PDF generation, synthetic monitoring
