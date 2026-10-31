import http from "node:http";
import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const publicDir = path.join(__dirname, "public");
const port = Number(process.env.PORT || 4317);
const baseUrl = process.env.BASE_URL || `http://localhost:${port}`;

const sessions = new Map();
const oauthStates = new Map();
const auditLog = [];

const skills = [
  {
    id: "legacy-brief",
    title: "Legacy Migration Brief",
    provider: "claude",
    description: "Build an inventory-first migration brief for COBOL, RPGLE, CL, or DB2 slices.",
    requiredInputs: ["artifactPath", "businessGoal"],
    hiddenPrompt:
      "You are a legacy modernization analyst. Inventory inputs, outputs, files, tables, jobs, reports, side effects, business rules, assumptions, and acceptance checks before suggesting code.",
    agentRoute: "claude-code:modernization-brief"
  },
  {
    id: "rpg-to-spring-plan",
    title: "RPG to Spring Plan",
    provider: "copilot",
    description: "Create a conservative Java/Kotlin Spring conversion plan with characterization tests.",
    requiredInputs: ["artifactPath", "targetStack"],
    hiddenPrompt:
      "You are a senior modernization engineer. Preserve RPG behavior first, map DB2 access explicitly, identify write boundaries, and propose focused characterization tests.",
    agentRoute: "github-copilot:workspace-agent"
  },
  {
    id: "code-review-gate",
    title: "AI Output Review Gate",
    provider: "claude",
    description: "Review generated modernization output against safety, behavior, and test criteria.",
    requiredInputs: ["changeSummary", "riskArea"],
    hiddenPrompt:
      "Review as a strict migration gate. Prioritize behavior regressions, unapproved database writes, missing acceptance checks, secret leakage, and unsupported assumptions.",
    agentRoute: "claude-code:review"
  },
  {
    id: "kql-investigation",
    title: "KQL Investigation",
    provider: "claude",
    description: "Generate or review KQL for Azure Monitor, Log Analytics, and Application Insights investigations.",
    requiredInputs: ["workspaceScope", "investigationGoal", "timeRange"],
    hiddenPrompt:
      "You are a KQL investigation specialist. Produce safe, scoped, readable Kusto queries for Azure Monitor, Log Analytics, and Application Insights. Ask for missing table names when required, prefer time-bounded queries, avoid destructive assumptions, explain joins/summarize/bin choices, and include validation steps for query results.",
    agentRoute: "claude-code:kql"
  },
  {
    id: "ebcdic-conversion",
    title: "EBCDIC Conversion",
    provider: "claude",
    description: "Analyze EBCDIC files, code pages, fixed-width layouts, and legacy data conversion risks.",
    requiredInputs: ["sourceEncoding", "recordLayout", "conversionGoal"],
    hiddenPrompt:
      "You are an EBCDIC and legacy data conversion specialist. Help analyze IBM mainframe and IBM i data files, code pages, fixed-width layouts, packed decimal, zoned decimal, signed numeric fields, and ASCII/UTF-8 conversion risks. Preserve bytes and business meaning, require sample records or copybooks when needed, avoid guessing code pages, and propose validation plus round-trip checks.",
    agentRoute: "claude-code:ebcdic"
  },
  {
    id: "mainframe-modernization",
    title: "Mainframe Modernization",
    provider: "claude",
    description: "Analyze COBOL, JCL, CICS, IMS, VSAM, DB2 z/OS, and batch modernization slices.",
    requiredInputs: ["mainframeArtifact", "platformContext", "modernizationGoal"],
    hiddenPrompt:
      "You are a mainframe modernization specialist. Analyze COBOL, JCL, CICS, IMS, VSAM, DB2 z/OS, batch schedules, copybooks, datasets, transactions, reports, and operational side effects. Preserve behavior before refactoring, identify inputs/outputs/dependencies, flag missing copybooks or control cards, propose characterization tests, and keep production writes or destructive changes gated behind explicit human approval.",
    agentRoute: "claude-code:mainframe"
  },
  {
    id: "vscode-ibmi-extensions",
    title: "VS Code IBM i Extensions",
    provider: "claude",
    description: "Plan and troubleshoot VS Code extension workflows for IBM i development.",
    requiredInputs: ["extensionGoal", "ibmiEnvironment", "developerWorkflow"],
    hiddenPrompt:
      "You are a VS Code for IBM i tooling specialist. Help configure, troubleshoot, and document extension workflows for IBM i development, including Code for IBM i, RPGLE/CL/COBOL editing, library lists, source members, Actions, object deployment, compile commands, SQL tools, terminals, and workspace settings. Avoid exposing credentials, prefer least-privilege connection setup, and require explicit approval before remote destructive IBM i commands.",
    agentRoute: "claude-code:vscode-ibmi"
  }
];

function publicSkill(skill) {
  const { hiddenPrompt, ...safeSkill } = skill;
  return safeSkill;
}

function json(res, status, body) {
  res.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store"
  });
  res.end(JSON.stringify(body));
}

function redirect(res, location) {
  res.writeHead(302, { location });
  res.end();
}

function parseCookies(req) {
  return Object.fromEntries(
    (req.headers.cookie || "")
      .split(";")
      .map((cookie) => cookie.trim())
      .filter(Boolean)
      .map((cookie) => {
        const index = cookie.indexOf("=");
        return [cookie.slice(0, index), decodeURIComponent(cookie.slice(index + 1))];
      })
  );
}

function currentSession(req) {
  const id = parseCookies(req).sid;
  return id ? sessions.get(id) : undefined;
}

function publicSession(session) {
  return session ? { user: session.user, createdAt: session.createdAt } : null;
}

function createSession(user) {
  const id = crypto.randomBytes(24).toString("hex");
  sessions.set(id, { id, user, createdAt: new Date().toISOString() });
  return id;
}

function setSessionCookie(res, sessionId) {
  res.setHeader("set-cookie", `sid=${encodeURIComponent(sessionId)}; HttpOnly; SameSite=Lax; Path=/`);
}

async function readBody(req) {
  const chunks = [];
  for await (const chunk of req) chunks.push(chunk);
  return Buffer.concat(chunks).toString("utf8");
}

async function serveStatic(req, res, pathname) {
  const safePath = pathname === "/" ? "/index.html" : pathname;
  const filePath = path.normalize(path.join(publicDir, safePath));
  if (!filePath.startsWith(publicDir)) return json(res, 403, { error: "Forbidden" });

  try {
    const data = await fs.readFile(filePath);
    const ext = path.extname(filePath);
    const type = {
      ".html": "text/html; charset=utf-8",
      ".css": "text/css; charset=utf-8",
      ".js": "application/javascript; charset=utf-8",
      ".svg": "image/svg+xml"
    }[ext] || "application/octet-stream";
    res.writeHead(200, { "content-type": type });
    res.end(data);
  } catch {
    json(res, 404, { error: "Not found" });
  }
}

function startOAuth(req, res, url) {
  let provider = url.searchParams.get("provider") || "demo";
  if (provider === "github" && !process.env.GITHUB_CLIENT_ID) {
    provider = "demo";
  }
  const state = crypto.randomBytes(18).toString("hex");
  oauthStates.set(state, { provider, createdAt: Date.now() });

  if (provider === "github" && process.env.GITHUB_CLIENT_ID) {
    const params = new URLSearchParams({
      client_id: process.env.GITHUB_CLIENT_ID,
      redirect_uri: `${baseUrl}/auth/callback?provider=github`,
      scope: "read:user user:email",
      state
    });
    return redirect(res, `https://github.com/login/oauth/authorize?${params}`);
  }

  const params = new URLSearchParams({ provider: "demo", code: "local-demo-user", state });
  redirect(res, `/auth/callback?${params}`);
}

async function finishOAuth(req, res, url) {
  const provider = url.searchParams.get("provider") || "demo";
  const state = url.searchParams.get("state") || "";
  const saved = oauthStates.get(state);
  oauthStates.delete(state);

  if (!saved || saved.provider !== provider) {
    return json(res, 401, { error: "Invalid OAuth state" });
  }

  let user = {
    id: "local-demo-user",
    name: "Local Demo User",
    provider: "demo"
  };

  if (provider === "github" && process.env.GITHUB_CLIENT_ID && process.env.GITHUB_CLIENT_SECRET) {
    const tokenResponse = await fetch("https://github.com/login/oauth/access_token", {
      method: "POST",
      headers: { accept: "application/json", "content-type": "application/json" },
      body: JSON.stringify({
        client_id: process.env.GITHUB_CLIENT_ID,
        client_secret: process.env.GITHUB_CLIENT_SECRET,
        code: url.searchParams.get("code"),
        redirect_uri: `${baseUrl}/auth/callback?provider=github`
      })
    });
    const token = await tokenResponse.json();
    if (!token.access_token) return json(res, 401, { error: "OAuth token exchange failed" });

    const userResponse = await fetch("https://api.github.com/user", {
      headers: {
        authorization: `Bearer ${token.access_token}`,
        accept: "application/vnd.github+json",
        "user-agent": "agent-gateway-web"
      }
    });
    const profile = await userResponse.json();
    user = {
      id: String(profile.id),
      name: profile.name || profile.login,
      login: profile.login,
      provider: "github"
    };
  }

  const sessionId = createSession(user);
  setSessionCookie(res, sessionId);
  redirect(res, "/");
}

async function runSkill(req, res) {
  const session = currentSession(req);
  if (!session) return json(res, 401, { error: "Sign in required" });

  const body = JSON.parse((await readBody(req)) || "{}");
  const skill = skills.find((item) => item.id === body.skillId);
  if (!skill) return json(res, 404, { error: "Unknown skill" });

  const inputs = body.inputs || {};
  const missing = skill.requiredInputs.filter((name) => !String(inputs[name] || "").trim());
  if (missing.length) return json(res, 400, { error: `Missing inputs: ${missing.join(", ")}` });

  const run = {
    id: crypto.randomUUID(),
    skillId: skill.id,
    provider: skill.provider,
    agentRoute: skill.agentRoute,
    user: session.user.name,
    createdAt: new Date().toISOString(),
    status: "ready-for-provider",
    visibleRequest: inputs,
    providerEnvelope: {
      route: skill.agentRoute,
      systemPrompt: "[hidden server-side]",
      userPayload: inputs
    }
  };

  const serverProviderEnvelope = {
    route: skill.agentRoute,
    systemPrompt: skill.hiddenPrompt,
    userPayload: inputs
  };

  auditLog.unshift({
    id: run.id,
    skillId: skill.id,
    provider: skill.provider,
    user: session.user.name,
    createdAt: run.createdAt,
    status: run.status
  });

  console.log(`Prepared ${run.id} for ${serverProviderEnvelope.route}`);

  json(res, 200, run);
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url || "/", baseUrl);

  try {
    if (url.pathname === "/auth/login") return startOAuth(req, res, url);
    if (url.pathname === "/auth/callback") return finishOAuth(req, res, url);
    if (url.pathname === "/auth/logout") {
      const sid = parseCookies(req).sid;
      if (sid) sessions.delete(sid);
      res.setHeader("set-cookie", "sid=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0");
      return redirect(res, "/");
    }

    if (url.pathname === "/api/session") return json(res, 200, { session: publicSession(currentSession(req)) });
    if (url.pathname === "/api/skills") return json(res, 200, { skills: skills.map(publicSkill) });
    if (url.pathname === "/api/audit") {
      if (!currentSession(req)) return json(res, 401, { error: "Sign in required" });
      return json(res, 200, { auditLog });
    }
    if (url.pathname === "/api/run" && req.method === "POST") return runSkill(req, res);

    return serveStatic(req, res, url.pathname);
  } catch (error) {
    json(res, 500, { error: error.message || "Unexpected error" });
  }
});

server.listen(port, () => {
  console.log(`Agent Gateway running at ${baseUrl}`);
});
