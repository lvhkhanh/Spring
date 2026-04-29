---
name: setupTests
description: '**WORKFLOW SKILL** — Configure and maintain shared test setup for application and library projects. USE FOR: creating or updating `setupTests` files, wiring global mocks and polyfills, registering custom matchers, bootstrapping test environments for Jest/Vitest/RTL, and standardizing test initialization across repositories. DO NOT USE FOR: writing feature-specific production logic, replacing focused test cases with global side effects, or configuring unrelated build/runtime environments. INVOKES: file system tools for config and test bootstrap files, terminal for test runner validation, semantic search for framework-specific setup conventions.'
---

# Test Setup Skill

## Overview

This skill provides structured support for creating and maintaining shared test initialization for JavaScript, TypeScript, and frontend application projects. It helps define `setupTests` files, register reusable test utilities, configure DOM and browser-like environments, add global mocks, and keep test bootstrap code stable, minimal, and easy to reason about.

## Key Capabilities

### Test Bootstrap Creation
- Create `setupTests.ts`, `setupTests.js`, or equivalent bootstrap files
- Wire test setup into Jest, Vitest, React Testing Library, and related runners
- Add shared imports for custom matchers and common utilities
- Keep initialization logic centralized and deterministic

### Environment Configuration
- Configure `jsdom`, browser-like globals, and runtime polyfills
- Initialize test-time environment variables where appropriate
- Set up fetch, ResizeObserver, IntersectionObserver, matchMedia, and other browser APIs
- Align framework config files with the selected test bootstrap entry point

### Global Mocks and Utilities
- Register safe default mocks for APIs that are noisy or unavailable in test
- Add cleanup hooks, spies, and reset behavior to prevent cross-test leakage
- Expose reusable render helpers and providers through shared setup patterns
- Support test-only shims without polluting production code paths

### Framework-Specific Guidance
- Configure Jest `setupFilesAfterEnv` and related options
- Configure Vitest `setupFiles`, `environment`, and globals behavior
- Support React Testing Library matcher setup via `@testing-library/jest-dom`
- Adapt setup patterns for Next.js, Vite, CRA, monorepos, and shared packages

### Stability and Maintainability
- Minimize hidden side effects in global setup
- Identify what belongs in `setupTests` versus per-test fixtures
- Prevent flaky tests caused by leaked mocks, timers, or async state
- Keep bootstrap code readable, explicit, and easy to debug

## Usage Examples

### Create a React Testing Setup
```
Create a `setupTests.ts` for a React project using Jest and React Testing Library.
It should register jest-dom, mock `matchMedia`, and reset mocks after each test.
```

### Configure Vitest Bootstrap
```
Set up Vitest for a Vite + TypeScript app with `jsdom`, a shared `setupTests.ts`,
and fetch/ResizeObserver test shims.
```

### Refactor Bloated Test Globals
```
Review this existing `setupTests.js` and separate global bootstrapping from
feature-specific mocks so tests stay isolated and easier to maintain.
```

### Add Missing Browser Polyfills
```
Our tests fail because `IntersectionObserver` and `scrollTo` are undefined.
Update the shared test setup with safe mocks and explain where they should live.
```

## Common Patterns

### Jest Configuration Pattern
```js
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.ts'],
};
```

### Vitest Configuration Pattern
```ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'jsdom',
    setupFiles: ['./src/setupTests.ts'],
    globals: true,
  },
});
```

### Minimal React Testing Library Setup
```ts
import '@testing-library/jest-dom';
import { afterEach, vi } from 'vitest';
import { cleanup } from '@testing-library/react';

afterEach(() => {
  cleanup();
  vi.restoreAllMocks();
});
```

### Safe Browser API Mock Pattern
```ts
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: (query: string) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: () => {},
    removeListener: () => {},
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => false,
  }),
});
```

## Best Practices

- Put only truly shared setup in `setupTests`; keep feature-specific mocks close to the tests that need them
- Reset mocks, timers, and DOM state between tests to avoid leakage
- Prefer lightweight shims over large global mock frameworks
- Match setup file naming and location to repository conventions
- Document non-obvious globals so future contributors know why they exist
- Revisit bootstrap code when changing test runners, frameworks, or DOM environment assumptions
- Keep setup idempotent so reruns and watch mode stay stable

## Troubleshooting

### Tests Pass Alone but Fail Together
- Check for leaked mocks, fake timers, and mutated globals
- Ensure cleanup/reset hooks run after each test
- Move scenario-specific state out of shared bootstrap

### Browser APIs Are Undefined
- Confirm the runner uses `jsdom` when DOM APIs are required
- Add only the missing mocks or polyfills needed by the test environment
- Keep mock behavior minimal unless tests rely on richer semantics

### Matchers or Globals Are Not Loaded
- Verify `setupFilesAfterEnv` or `setupFiles` points to the correct file
- Check path resolution in monorepos and package-local configs
- Confirm the bootstrap file is included in the active test runner config

### Setup File Became a Dumping Ground
- Split reusable helpers into dedicated test utility modules
- Keep `setupTests` focused on registration and environment bootstrapping
- Remove stale mocks that no longer support active tests

## Integration Points

- **Test runners**: Jest, Vitest
- **UI testing**: React Testing Library, jsdom
- **Frameworks**: React, Next.js, Vite, Create React App
- **Shared utilities**: custom render helpers, provider wrappers, mock servers
- **Quality workflows**: CI pipelines, watch mode, pre-merge test validation
