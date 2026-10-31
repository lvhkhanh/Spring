# Agent Gateway Web

Tiny OAuth-gated web wrapper for predefined skills, prompts, and agent routes. It hides provider prompts on the server and exposes only approved skills in the browser.

## What It Does

- Requires login before running a skill.
- Supports local demo OAuth and optional GitHub OAuth.
- Shows a predefined skill catalog for Claude/Copilot-style routing.
- Builds a provider envelope containing the hidden system prompt, route, and user inputs.
- Keeps an in-memory audit log of skill runs.
- Includes a Claude-routed KQL investigation skill for Azure Monitor, Log Analytics, and Application Insights.
- Includes a Claude-routed EBCDIC conversion skill for legacy file encoding and record-layout analysis.
- Includes a Claude-routed mainframe modernization skill for COBOL, JCL, CICS, IMS, VSAM, and DB2 z/OS analysis.
- Includes a Claude-routed VS Code IBM i extensions skill for Code for IBM i, RPGLE/CL editing, compile actions, and workspace setup.

This prototype does not call Claude or Copilot directly. The `providerEnvelope` is the integration boundary where a real provider adapter can be added.

## Run

```bash
cd ai-native/agent-gateway-web
npm start
```

Open `http://localhost:4317`.

## Optional GitHub OAuth

Create a GitHub OAuth app with callback URL:

```text
http://localhost:4317/auth/callback?provider=github
```

Then start with:

```bash
GITHUB_CLIENT_ID=... GITHUB_CLIENT_SECRET=... npm start
```

If these variables are absent, the GitHub login button falls back to the local demo OAuth flow.

## Extension/Desktop Path

The current app is intentionally plain web. To turn it into a VS Code extension or desktop app later:

- Keep `server.js` as the local gateway process.
- Render `public/` inside a VS Code webview or Electron shell.
- Replace `providerEnvelope` return values with provider adapters for Claude Code, GitHub Copilot workspace actions, or an internal agent runner.
- Persist audit records in a local encrypted store instead of memory.
