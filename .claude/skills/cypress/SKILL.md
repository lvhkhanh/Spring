---
name: cypress
description: '**WORKFLOW SKILL** — Create, refactor, optimize, debug, and maintain Cypress end-to-end and component tests for web applications. USE FOR: writing reliable test suites, designing page object and app action patterns, handling authentication and API mocking, testing responsive layouts, integrating with CI/CD pipelines, debugging flaky tests, managing test data, and validating accessibility. DO NOT USE FOR: unit testing pure functions without DOM (use Jest/Vitest), load/performance testing (use k6/Artillery), or native mobile testing (use Appium/Detox). INVOKES: file system tools for test and config files, terminal for cypress CLI commands, browser tools for visual verification, and test result analysis.'
---

# Cypress Testing Skill

## Overview

This skill provides comprehensive support for Cypress end-to-end and component testing across modern web applications built with React, Angular, Vue, Next.js, and other frameworks. It helps author reliable tests, design maintainable test architectures, handle complex scenarios like authentication and API interception, debug flaky tests, integrate with CI/CD pipelines, and enforce testing best practices that keep suites fast, stable, and trustworthy.

## Key Capabilities

### Test Authoring
- Write end-to-end tests with `cy.visit`, `cy.get`, `cy.contains`, assertions, and action commands
- Build component tests using `cy.mount` for isolated component validation
- Chain commands idiomatically with Cypress's retry-and-timeout model
- Implement custom commands for reusable test actions

### Selectors and Querying
- Use `data-cy`, `data-testid`, or `data-test` attributes for resilient selectors
- Query with `cy.get`, `cy.contains`, `cy.find`, `cy.within`, and `cy.closest`
- Handle shadow DOM, iframes, and dynamically rendered content
- Avoid brittle selectors tied to CSS classes, tag hierarchies, or text that changes with i18n

### Network and API
- Intercept HTTP requests with `cy.intercept` for stubbing, spying, and waiting
- Mock API responses for deterministic test data
- Test error states, loading states, and timeout behavior
- Validate request payloads sent by the application

### Authentication and Session
- Use `cy.session` for cached authentication across tests
- Implement programmatic login via API calls instead of UI login flows
- Handle OAuth, SSO, and multi-factor authentication patterns
- Manage cookies, localStorage, and sessionStorage

### Assertions and Validation
- Use Chai, Chai-jQuery, and Sinon-Chai assertions via `should` and `expect`
- Assert visibility, text content, attributes, CSS properties, and element state
- Validate URL, page title, and navigation behavior
- Test file downloads, clipboard operations, and browser events

### CI/CD Integration
- Configure headless execution with `cypress run`
- Parallelize test suites across multiple containers
- Record results to Cypress Cloud or alternative dashboards
- Generate JUnit, Mochawesome, or custom reports
- Handle video and screenshot artifacts

### Debugging and Stability
- Diagnose and fix flaky tests caused by timing, animation, or network races
- Use `cy.wait`, `cy.intercept` aliases, and retry-able assertions instead of arbitrary waits
- Leverage Cypress DevTools, `cy.debug`, `cy.pause`, and time-travel snapshots
- Identify and resolve detached DOM element errors

## Usage Examples

### Write a login flow test
```
Write a Cypress E2E test that logs in via the UI, verifies the dashboard loads, and checks that the user's name appears in the header.
```

### Test form validation
```
Create Cypress tests for a registration form covering required fields, email format, password strength, matching passwords, and server-side validation errors.
```

### Mock API responses
```
Write a Cypress test that intercepts the GET /api/products endpoint, returns a stubbed response with 3 products, and verifies the product list renders correctly.
```

### Test responsive layout
```
Create Cypress tests that verify the navigation menu collapses into a hamburger menu on mobile viewport and expands on desktop viewport.
```

### Debug a flaky test
```
This Cypress test intermittently fails with "element is detached from the DOM". Diagnose the root cause and fix it.
```

### Set up CI pipeline
```
Add a GitHub Actions workflow that runs Cypress tests in parallel across 3 containers with video recording and Mochawesome reports.
```

## Common Patterns

### Basic E2E test structure
```javascript
describe('User Dashboard', () => {
  beforeEach(() => {
    cy.loginAsUser('testuser@example.com');
    cy.visit('/dashboard');
  });

  it('displays the welcome message with user name', () => {
    cy.get('[data-cy="welcome-message"]')
      .should('be.visible')
      .and('contain', 'Welcome, Test User');
  });

  it('shows recent activity list', () => {
    cy.get('[data-cy="activity-list"]')
      .should('be.visible')
      .find('[data-cy="activity-item"]')
      .should('have.length.at.least', 1);
  });

  it('navigates to profile on avatar click', () => {
    cy.get('[data-cy="user-avatar"]').click();
    cy.url().should('include', '/profile');
    cy.get('[data-cy="profile-heading"]')
      .should('contain', 'Test User');
  });
});
```

### Custom command for login
```javascript
// cypress/support/commands.js
Cypress.Commands.add('loginAsUser', (email, password = 'TestPassword123!') => {
  cy.session(
    email,
    () => {
      cy.request({
        method: 'POST',
        url: '/api/auth/login',
        body: { email, password },
      }).then(({ body }) => {
        window.localStorage.setItem('authToken', body.token);
        window.localStorage.setItem('user', JSON.stringify(body.user));
      });
    },
    {
      validate() {
        cy.request({
          url: '/api/auth/me',
          failOnStatusCode: false,
        }).its('status').should('eq', 200);
      },
    }
  );
});
```

### API interception and stubbing
```javascript
describe('Product List', () => {
  const mockProducts = [
    { id: 1, name: 'Widget A', price: 29.99, inStock: true },
    { id: 2, name: 'Widget B', price: 49.99, inStock: false },
    { id: 3, name: 'Widget C', price: 19.99, inStock: true },
  ];

  beforeEach(() => {
    cy.intercept('GET', '/api/products', {
      statusCode: 200,
      body: { data: mockProducts },
    }).as('getProducts');

    cy.visit('/products');
    cy.wait('@getProducts');
  });

  it('renders all products', () => {
    cy.get('[data-cy="product-card"]')
      .should('have.length', 3);
  });

  it('shows out-of-stock badge for unavailable products', () => {
    cy.get('[data-cy="product-card"]')
      .contains('Widget B')
      .closest('[data-cy="product-card"]')
      .find('[data-cy="out-of-stock-badge"]')
      .should('be.visible');
  });

  it('handles API error gracefully', () => {
    cy.intercept('GET', '/api/products', {
      statusCode: 500,
      body: { error: 'Internal Server Error' },
    }).as('getProductsError');

    cy.visit('/products');
    cy.wait('@getProductsError');

    cy.get('[data-cy="error-message"]')
      .should('be.visible')
      .and('contain', 'Failed to load products');

    cy.get('[data-cy="retry-button"]')
      .should('be.visible');
  });
});
```

### Request validation (spy pattern)
```javascript
it('sends correct payload when creating an order', () => {
  cy.intercept('POST', '/api/orders').as('createOrder');

  cy.get('[data-cy="product-card"]').first().find('[data-cy="add-to-cart"]').click();
  cy.get('[data-cy="checkout-button"]').click();
  cy.get('[data-cy="confirm-order"]').click();

  cy.wait('@createOrder').then(({ request }) => {
    expect(request.body).to.have.property('items');
    expect(request.body.items).to.have.length(1);
    expect(request.body.items[0]).to.have.property('productId', 1);
    expect(request.headers).to.have.property('authorization');
  });
});
```

### Responsive viewport testing
```javascript
describe('Navigation Menu', () => {
  beforeEach(() => {
    cy.visit('/');
  });

  context('desktop viewport', () => {
    beforeEach(() => {
      cy.viewport(1280, 720);
    });

    it('shows horizontal nav links', () => {
      cy.get('[data-cy="nav-links"]').should('be.visible');
      cy.get('[data-cy="hamburger-menu"]').should('not.be.visible');
    });
  });

  context('mobile viewport', () => {
    beforeEach(() => {
      cy.viewport('iphone-x');
    });

    it('shows hamburger menu and hides nav links', () => {
      cy.get('[data-cy="hamburger-menu"]').should('be.visible');
      cy.get('[data-cy="nav-links"]').should('not.be.visible');
    });

    it('opens mobile menu on hamburger click', () => {
      cy.get('[data-cy="hamburger-menu"]').click();
      cy.get('[data-cy="mobile-nav"]')
        .should('be.visible')
        .find('a')
        .should('have.length.at.least', 3);
    });
  });
});
```

### Form validation testing
```javascript
describe('Registration Form', () => {
  beforeEach(() => {
    cy.visit('/register');
  });

  it('shows validation errors for empty required fields', () => {
    cy.get('[data-cy="submit-register"]').click();

    cy.get('[data-cy="error-email"]').should('contain', 'Email is required');
    cy.get('[data-cy="error-password"]').should('contain', 'Password is required');
  });

  it('validates email format', () => {
    cy.get('[data-cy="input-email"]').type('not-an-email');
    cy.get('[data-cy="submit-register"]').click();

    cy.get('[data-cy="error-email"]').should('contain', 'Invalid email');
  });

  it('validates password strength', () => {
    cy.get('[data-cy="input-password"]').type('weak');
    cy.get('[data-cy="submit-register"]').click();

    cy.get('[data-cy="error-password"]')
      .should('contain', 'at least 8 characters');
  });

  it('submits successfully with valid data', () => {
    cy.intercept('POST', '/api/auth/register', {
      statusCode: 201,
      body: { message: 'Account created' },
    }).as('register');

    cy.get('[data-cy="input-email"]').type('new@example.com');
    cy.get('[data-cy="input-password"]').type('StrongPass123!');
    cy.get('[data-cy="input-confirm-password"]').type('StrongPass123!');
    cy.get('[data-cy="submit-register"]').click();

    cy.wait('@register');
    cy.url().should('include', '/login');
    cy.get('[data-cy="success-message"]')
      .should('contain', 'Account created');
  });
});
```

### Page Object / App Action pattern
```javascript
// cypress/support/pages/LoginPage.js
export class LoginPage {
  visit() {
    cy.visit('/login');
    return this;
  }

  getEmailInput() {
    return cy.get('[data-cy="input-email"]');
  }

  getPasswordInput() {
    return cy.get('[data-cy="input-password"]');
  }

  getSubmitButton() {
    return cy.get('[data-cy="submit-login"]');
  }

  getErrorMessage() {
    return cy.get('[data-cy="login-error"]');
  }

  login(email, password) {
    this.getEmailInput().clear().type(email);
    this.getPasswordInput().clear().type(password);
    this.getSubmitButton().click();
    return this;
  }
}

// cypress/e2e/login.cy.js
import { LoginPage } from '../support/pages/LoginPage';

describe('Login', () => {
  const loginPage = new LoginPage();

  it('logs in with valid credentials', () => {
    loginPage.visit().login('user@example.com', 'ValidPass123!');
    cy.url().should('include', '/dashboard');
  });

  it('shows error for invalid credentials', () => {
    loginPage.visit().login('user@example.com', 'WrongPassword');
    loginPage.getErrorMessage()
      .should('be.visible')
      .and('contain', 'Invalid credentials');
  });
});
```

### Waiting for network with aliases
```javascript
it('loads and displays user profile', () => {
  cy.intercept('GET', '/api/user/profile').as('getProfile');
  cy.intercept('GET', '/api/user/preferences').as('getPreferences');

  cy.visit('/profile');

  // Wait for both API calls to complete
  cy.wait(['@getProfile', '@getPreferences']);

  cy.get('[data-cy="profile-name"]').should('not.be.empty');
  cy.get('[data-cy="preferences-section"]').should('be.visible');
});
```

### File upload testing
```javascript
it('uploads a profile avatar', () => {
  cy.intercept('POST', '/api/user/avatar').as('uploadAvatar');

  cy.get('[data-cy="avatar-input"]').selectFile('cypress/fixtures/avatar.png');
  cy.get('[data-cy="upload-button"]').click();

  cy.wait('@uploadAvatar').its('response.statusCode').should('eq', 200);
  cy.get('[data-cy="avatar-preview"]')
    .should('be.visible')
    .and('have.attr', 'src')
    .and('not.be.empty');
});
```

### Handling tables and lists
```javascript
it('sorts the user table by name', () => {
  cy.get('[data-cy="table-header-name"]').click();

  cy.get('[data-cy="table-row"]').then(($rows) => {
    const names = [...$rows].map(
      (row) => row.querySelector('[data-cy="cell-name"]').textContent
    );
    const sorted = [...names].sort();
    expect(names).to.deep.equal(sorted);
  });
});

it('paginates through results', () => {
  cy.get('[data-cy="table-row"]').should('have.length', 10);
  cy.get('[data-cy="page-2"]').click();
  cy.get('[data-cy="table-row"]').should('have.length.at.least', 1);
  cy.url().should('include', 'page=2');
});
```

## Configuration

### cypress.config.js
```javascript
const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    specPattern: 'cypress/e2e/**/*.cy.{js,ts}',
    supportFile: 'cypress/support/e2e.js',
    viewportWidth: 1280,
    viewportHeight: 720,
    defaultCommandTimeout: 10000,
    requestTimeout: 15000,
    responseTimeout: 15000,
    video: true,
    screenshotOnRunFailure: true,
    retries: {
      runMode: 2,    // retry in CI
      openMode: 0,   // no retry in interactive mode
    },
    env: {
      apiUrl: 'http://localhost:3001',
    },
    setupNodeEvents(on, config) {
      // Register plugins here
      return config;
    },
  },

  component: {
    devServer: {
      framework: 'react',
      bundler: 'vite',
    },
    specPattern: 'src/**/*.cy.{js,ts,jsx,tsx}',
  },
});
```

### Project structure
```
cypress/
  e2e/                      # End-to-end test specs
    auth/
      login.cy.js
      register.cy.js
    dashboard/
      overview.cy.js
    products/
      list.cy.js
      detail.cy.js
  fixtures/                  # Static test data (JSON, images)
    users.json
    products.json
    avatar.png
  support/
    commands.js              # Custom commands
    e2e.js                   # Support file loaded before each E2E spec
    component.js             # Support file for component tests
    pages/                   # Page objects
      LoginPage.js
      DashboardPage.js
  downloads/                 # Downloaded file assertions
cypress.config.js
```

## Best Practices

### Selectors
- Use `data-cy` attributes as the primary selector strategy — they survive CSS refactors and framework changes
- Never select by CSS class, inline style, or deeply nested tag paths
- Use `cy.contains` for user-visible text only when the text is stable and unique
- Use `cy.within` to scope queries to a specific container and avoid ambiguous matches

### Test independence
- Each test must be able to run in isolation — never depend on a previous test's side effects
- Use `beforeEach` for shared setup, not `before` (which runs once per suite)
- Reset application state before each test: seed database, clear storage, or stub APIs
- Never share mutable state between `it` blocks

### Network handling
- Always intercept API calls and use `cy.wait('@alias')` instead of `cy.wait(milliseconds)`
- Stub API responses for speed and determinism in most tests
- Keep a small set of "real API" integration tests that hit the actual backend
- Test loading states by adding `delay` to intercept responses
- Test error states by returning 4xx/5xx from intercepts

### Assertions
- Use `.should()` for retry-able assertions — Cypress retries until timeout
- Prefer specific assertions: `.should('have.text', 'Hello')` over `.should('contain', 'H')`
- Assert on visible user outcomes, not internal application state
- Avoid `.then()` for assertions that `.should()` can handle — `.then()` does not retry

### Authentication
- Use `cy.session` to cache login state across tests — avoids repeating login UI flow
- Perform login via API (programmatic) rather than clicking through the login form
- Validate sessions in the `validate` callback to ensure cached state is still valid
- Reserve UI login tests for the login page spec only

### Flaky test prevention
- Never use `cy.wait(N)` with a fixed millisecond timeout — always wait for a network alias or DOM condition
- Use `{ force: true }` only as a last resort; fix the underlying visibility issue instead
- Handle animations with `cy.get(..., { timeout: ... })` or disable animations in test mode
- Guard against detached DOM by querying elements after the action that causes re-render
- Use `retries` config for CI runs, but investigate and fix the root cause of failures

### Test data
- Use fixtures for static test data and factory functions for dynamic data
- Keep test data minimal — only include fields the test actually needs
- Isolate test data per test to avoid cross-contamination
- Use `cy.intercept` to control data rather than relying on shared database state

### Performance
- Keep individual tests under 30 seconds; split long flows into focused specs
- Use `cy.session` to skip repeated login flows
- Stub heavy or slow APIs in most tests
- Run tests in parallel across multiple containers in CI
- Use `--spec` to run only changed test files during development

## Troubleshooting

### Common errors
- **`cy.get()` timed out**: element not in DOM or not visible — check selector, wait for API response, increase timeout, or verify the page rendered
- **Element is detached from the DOM**: React/Vue re-rendered between query and action — re-query the element after the state change
- **`cy.intercept` not matching**: URL pattern, method, or timing mismatch — verify the exact URL with DevTools and set up the intercept before the action that triggers the request
- **Cross-origin error**: Cypress cannot visit two different origins in one test — use `cy.origin()` (Cypress 12+) or restructure the test
- **`cy.session` validation fails**: cached state expired or was invalidated — check token expiry and session storage consistency

### Selector issues
- **Multiple elements matched**: selector is not specific enough — scope with `cy.within` or add a unique `data-cy` attribute
- **Element found but not interactable**: covered by another element, hidden, or disabled — scroll into view, close modals, or wait for animations
- **Shadow DOM element not found**: use `{ includeShadowDom: true }` option or `cy.get().shadow()`

### Network and timing
- **Test passes locally but fails in CI**: timing differences — replace `cy.wait(ms)` with `cy.wait('@alias')`, increase timeouts, or add explicit assertions
- **Stubbed response not used**: intercept was set up after the request fired — move `cy.intercept` before `cy.visit` or the triggering action
- **WebSocket or SSE not interceptable**: Cypress intercept only supports HTTP — use application-level test hooks for WebSocket testing

### CI/CD issues
- **Tests timeout in CI**: headless Chrome needs more resources — increase container memory/CPU, reduce parallelism, or split large spec files
- **Video recording shows blank screen**: application failed to start — check `baseUrl` accessibility and startup timing
- **Screenshots not captured on failure**: `screenshotOnRunFailure` is false or disk space is full — check config and CI artifact storage

## Integration Points

- Frameworks: React, Angular, Vue, Next.js, Nuxt, Svelte, Remix
- Bundlers: Vite, Webpack, esbuild (for component testing dev server)
- CI/CD: GitHub Actions, GitLab CI, Azure DevOps, Jenkins, CircleCI, Bitbucket Pipelines
- Reporting: Cypress Cloud, Mochawesome, JUnit XML, Allure
- Visual testing: Percy, Applitools, Cypress Visual Testing plugin
- Accessibility: cypress-axe, pa11y
- Code coverage: @cypress/code-coverage with Istanbul/nyc
- Authentication: Auth0, Okta, AWS Cognito, Firebase Auth
- API mocking: cy.intercept (built-in), MSW (for shared mocks with unit tests)
- Database: cy.task for database seeding/cleanup via Node.js plugins
