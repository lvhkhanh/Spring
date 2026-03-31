---
name: chrome
description: '**WORKFLOW SKILL** — Create, develop, debug, and optimize Google Chrome extensions, DevTools usage, and browser automation. USE FOR: Chrome extension development; manifest configuration; content scripts and background scripts; Chrome DevTools debugging; browser automation with Puppeteer/Playwright; extension publishing and distribution. DO NOT USE FOR: general web development; non-Chrome browser development; server-side automation. INVOKES: file system tools for extension creation/modification, terminal for build/testing commands, semantic search for extension patterns.'
---

# Chrome Development

## Overview

This skill provides comprehensive support for Google Chrome development, including Chrome extension creation, DevTools usage, browser automation, and extension publishing.

## Key Capabilities

### Chrome Extension Development
- Generate complete extension structures from requirements
- Create manifest.json files with proper permissions
- Implement content scripts, background scripts, and popup pages
- Handle cross-origin requests and security policies

### DevTools & Debugging
- Chrome DevTools usage for debugging web applications
- Performance analysis and optimization
- Network monitoring and request inspection
- Console debugging and error tracking

### Browser Automation
- Puppeteer and Playwright script development
- Automated testing and scraping
- Screenshot and PDF generation
- Headless browser operations

### Extension Publishing
- Prepare extensions for Chrome Web Store submission
- Handle extension updates and versioning
- Manage extension permissions and privacy policies

## Usage Examples

### Creating a Basic Chrome Extension
```
Create a Chrome extension that:
- Shows a popup with current tab information
- Allows users to save bookmarks with custom tags
- Syncs data across devices using Chrome storage
- Includes a content script for page analysis
```

### Browser Automation Script
```javascript
// Puppeteer script for automated testing
const puppeteer = require('puppeteer');

async function runAutomation() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  await page.goto('https://example.com');
  await page.screenshot({ path: 'screenshot.png' });
  
  await browser.close();
}
```

### Extension Manifest Configuration
```json
{
  "manifest_version": 3,
  "name": "My Chrome Extension",
  "version": "1.0",
  "description": "A useful Chrome extension",
  "permissions": ["activeTab", "storage"],
  "action": {
    "default_popup": "popup.html"
  },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content.js"]
  }]
}
```

## Common Patterns

### Extension Architecture
```javascript
// background.js - Service worker for background tasks
chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension installed');
});

// content.js - Content script for page interaction
function injectScript() {
  const script = document.createElement('script');
  script.src = chrome.runtime.getURL('injected.js');
  document.head.appendChild(script);
}

// popup.js - Popup page logic
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('saveBtn').addEventListener('click', saveData);
});
```

### Browser Automation with Playwright
```javascript
const { chromium } = require('playwright');

async function automateBrowser() {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  
  // Navigate and interact
  await page.goto('https://example.com');
  await page.fill('input[name="search"]', 'query');
  await page.click('button[type="submit"]');
  
  // Wait for results
  await page.waitForSelector('.results');
  
  await browser.close();
}
```

### DevTools Console Commands
```javascript
// Performance monitoring
console.time('operation');
// ... code to measure ...
console.timeEnd('operation');

// Network analysis
fetch('/api/data')
  .then(response => response.json())
  .then(data => console.table(data));

// DOM inspection
$$('.elements').forEach(el => {
  console.log(el.textContent);
});
```

## Best Practices

### Extension Development
- Use Manifest V3 for new extensions
- Minimize permissions to only what's necessary
- Implement proper error handling and logging
- Test across different Chrome versions
- Follow Chrome Web Store policies

### Performance Optimization
- Use efficient DOM queries and event listeners
- Minimize background script execution
- Implement lazy loading for resources
- Cache frequently accessed data

### Security Considerations
- Validate all user inputs
- Use HTTPS for external communications
- Implement Content Security Policy
- Avoid eval() and innerHTML when possible

### Browser Automation
- Use headless mode for CI/CD pipelines
- Implement proper wait strategies
- Handle network timeouts gracefully
- Clean up browser instances

## Troubleshooting

### Extension Issues
- **Extension not loading**: Check manifest.json syntax and required fields
- **Permissions denied**: Verify manifest permissions match usage
- **Content scripts not working**: Check matches patterns and injection timing
- **Storage not persisting**: Ensure proper chrome.storage API usage

### DevTools Problems
- **Console errors**: Check for JavaScript syntax and runtime errors
- **Network failures**: Verify CORS policies and request headers
- **Performance issues**: Use Performance tab to identify bottlenecks
- **Memory leaks**: Monitor heap usage and garbage collection

### Automation Challenges
- **Element not found**: Use proper selectors and wait strategies
- **Timeouts**: Adjust timeout values and implement retry logic
- **Anti-bot detection**: Add human-like delays and behavior
- **Browser crashes**: Monitor resource usage and implement cleanup

### Publishing Issues
- **Rejected by Web Store**: Review policies and fix violations
- **Update failures**: Check version numbering and manifest compatibility
- **User reports**: Monitor reviews and address common complaints

## Integration Points

### Development Tools
- **VS Code**: Chrome extension development with debugging
- **Chrome DevTools**: Built-in debugging and performance tools
- **Webpack/Rollup**: Build tools for extension bundling
- **ESLint/Prettier**: Code quality and formatting

### Browser APIs
- **Chrome Extensions API**: Core extension functionality
- **WebExtensions API**: Cross-browser compatibility
- **Chrome DevTools Protocol**: Advanced debugging capabilities

### Automation Frameworks
- **Puppeteer**: Node.js browser automation
- **Playwright**: Cross-browser automation testing
- **Selenium WebDriver**: Traditional browser automation
- **Cypress**: End-to-end testing framework

### Cloud Services
- **Chrome Web Store**: Extension publishing platform
- **Firebase**: Backend services for extensions
- **AWS Lambda**: Serverless functions for extension backends
- **Google Cloud Functions**: Cloud-based extension services

### Testing & CI/CD
- **Jest/Mocha**: Unit testing for extension code
- **Chrome Extension Tester**: Extension-specific testing tools
- **GitHub Actions**: Automated testing and deployment
- **Chrome Web Store API**: Programmatic publishing

### Analytics & Monitoring
- **Google Analytics**: Extension usage tracking
- **Chrome Web Store Analytics**: Download and usage metrics
- **Sentry**: Error tracking and monitoring
- **Custom telemetry**: Extension-specific analytics