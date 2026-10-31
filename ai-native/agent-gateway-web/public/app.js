const authEl = document.querySelector("#auth");
const skillsEl = document.querySelector("#skills");
const formEl = document.querySelector("#runForm");
const resultEl = document.querySelector("#result");
const titleEl = document.querySelector("#title");
const providerEl = document.querySelector("#provider");
const descriptionEl = document.querySelector("#description");
const statusEl = document.querySelector("#status");
const auditEl = document.querySelector("#audit");
const copyEl = document.querySelector("#copy");

let session = null;
let skills = [];
let selectedSkill = null;

async function getJson(url, options) {
  const response = await fetch(url, options);
  const body = await response.json();
  if (!response.ok) throw new Error(body.error || "Request failed");
  return body;
}

function renderAuth() {
  if (!session) {
    authEl.innerHTML = `
      <a href="/auth/login?provider=demo"><button>Demo OAuth</button></a>
      <a href="/auth/login?provider=github"><button class="secondary">GitHub OAuth</button></a>
    `;
    statusEl.textContent = "Locked";
    statusEl.classList.remove("ready");
    return;
  }

  authEl.innerHTML = `
    <span class="status ready">${session.user.name}</span>
    <a href="/auth/logout"><button class="secondary">Sign out</button></a>
  `;
  statusEl.textContent = "Ready";
  statusEl.classList.add("ready");
}

function renderSkills() {
  document.querySelector("#skillCount").textContent = String(skills.length);
  skillsEl.innerHTML = skills
    .map(
      (skill) => `
        <button class="skill ${selectedSkill?.id === skill.id ? "active" : ""}" data-skill="${skill.id}">
          <strong>${skill.title}</strong>
          <span>${skill.description}</span>
        </button>
      `
    )
    .join("");

  skillsEl.querySelectorAll("[data-skill]").forEach((button) => {
    button.addEventListener("click", () => selectSkill(button.dataset.skill));
  });
}

function selectSkill(skillId) {
  selectedSkill = skills.find((skill) => skill.id === skillId);
  renderSkills();

  titleEl.textContent = selectedSkill.title;
  providerEl.textContent = `${selectedSkill.provider} via ${selectedSkill.agentRoute}`;
  descriptionEl.textContent = selectedSkill.description;
  formEl.innerHTML = selectedSkill.requiredInputs
    .map(
      (name) => `
        <label>
          ${labelFor(name)}
          <textarea name="${name}" placeholder="${placeholderFor(name)}"></textarea>
        </label>
      `
    )
    .join("") + `<button type="submit" ${session ? "" : "disabled"}>Generate provider payload</button>`;
}

function labelFor(name) {
  return name.replace(/([A-Z])/g, " $1").replace(/^./, (char) => char.toUpperCase());
}

function placeholderFor(name) {
  const examples = {
    artifactPath: "apps/RPG/EMPCRUD.rpgle",
    businessGoal: "Preserve employee CRUD behavior while planning a Spring API migration.",
    targetStack: "Kotlin, Spring Boot, DB2 repository layer",
    changeSummary: "Generated EmployeeService and tests from the RPG sample.",
    riskArea: "DB2 writes, behavior parity, missing validation",
    workspaceScope: "Application Insights workspace for demo2 / production API logs",
    investigationGoal: "Find failed requests and correlated exceptions after the latest deployment.",
    timeRange: "Last 24 hours",
    sourceEncoding: "IBM037, IBM500, IBM1047, or unknown EBCDIC code page",
    recordLayout: "COBOL copybook, RPG DDS layout, fixed-width field map, or sample hex dump",
    conversionGoal: "Convert customer master records to UTF-8 CSV while preserving packed decimals and signed fields.",
    mainframeArtifact: "COBOL program, JCL job, PROC, copybook, CICS transaction, VSAM layout, or DB2 SQL section",
    platformContext: "z/OS batch with JCL, CICS online transaction, IMS program, VSAM files, or DB2 z/OS tables",
    modernizationGoal: "Create an inventory-first migration brief and test plan before converting to Java/Spring.",
    extensionGoal: "Set up VS Code for RPGLE, CL, SQL, source members, compile actions, and object browsing.",
    ibmiEnvironment: "IBM i 7.4 or 7.5, SSH enabled, developer profile with limited library/object authority.",
    developerWorkflow: "Edit RPGLE locally, deploy to source physical file, compile, inspect job logs, and run SQL validation."
  };
  return examples[name] || "Required input";
}

async function renderAudit() {
  if (!session) {
    auditEl.innerHTML = "";
    document.querySelector("#auditCount").textContent = "0";
    return;
  }

  const { auditLog } = await getJson("/api/audit");
  document.querySelector("#auditCount").textContent = String(auditLog.length);
  auditEl.innerHTML = auditLog.length
    ? auditLog
        .map(
          (item) => `
            <div class="audit-item">
              <strong>${item.skillId}</strong>
              ${item.provider} · ${new Date(item.createdAt).toLocaleString()}
            </div>
          `
        )
        .join("")
    : `<p class="description">No runs yet.</p>`;
}

formEl.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!selectedSkill) return;

  const inputs = Object.fromEntries(new FormData(formEl).entries());
  resultEl.textContent = "Generating...";

  try {
    const run = await getJson("/api/run", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ skillId: selectedSkill.id, inputs })
    });
    resultEl.textContent = JSON.stringify(run.providerEnvelope, null, 2);
    await renderAudit();
  } catch (error) {
    resultEl.textContent = JSON.stringify({ error: error.message }, null, 2);
  }
});

copyEl.addEventListener("click", async () => {
  await navigator.clipboard.writeText(resultEl.textContent);
  copyEl.textContent = "Copied";
  setTimeout(() => {
    copyEl.textContent = "Copy";
  }, 1000);
});

async function boot() {
  const sessionResponse = await getJson("/api/session");
  session = sessionResponse.session;
  renderAuth();

  const skillsResponse = await getJson("/api/skills");
  skills = skillsResponse.skills;
  selectSkill(skills[0].id);
  await renderAudit();
}

boot().catch((error) => {
  resultEl.textContent = JSON.stringify({ error: error.message }, null, 2);
});
