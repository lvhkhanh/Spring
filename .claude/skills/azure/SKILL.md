---
name: azure
description: '**WORKFLOW SKILL** — Create, deploy, and manage Microsoft Azure applications and infrastructure. USE FOR: Azure service configuration, Functions/App Service/AKS deployment, Storage and SQL management, Entra ID and RBAC setup, and infrastructure as code. DO NOT USE FOR: non-Azure cloud platforms, general programming, or local development unrelated to Azure services. INVOKES: terminal for Azure CLI commands, file system tools for configuration files, semantic search for Azure patterns.'
---

# Microsoft Azure Development Skill

## Overview

This skill provides comprehensive support for Microsoft Azure development, deployment, and operations. It covers infrastructure as code, serverless and container workloads, data platforms, and cloud-native application practices with emphasis on security, reliability, and cost control.

## Key Capabilities

### Infrastructure as Code
- Provision Resource Groups, Virtual Networks, and subnets
- Deploy App Service, AKS, and Azure Functions workloads
- Configure Storage Accounts, Key Vault, and Service Bus
- Manage RBAC roles, managed identities, and policy controls

### Application Development
- Build serverless applications with Azure Functions and Logic Apps
- Deploy containerized services with Azure Container Apps and AKS
- Expose APIs through API Management and Application Gateway
- Implement event-driven workflows with Event Grid and Service Bus

### Data & Analytics
- Design and optimize Azure SQL and Cosmos DB usage
- Build pipelines with Azure Data Factory and Synapse
- Store and process files with Blob Storage and Data Lake
- Create observability dashboards with Azure Monitor and Log Analytics

### DevOps & Operations
- Set up CI/CD with GitHub Actions or Azure DevOps Pipelines
- Configure monitoring, alerts, and distributed tracing
- Implement secure secret management with Azure Key Vault
- Track and optimize spend with Cost Management + Billing

## Usage Examples

### Create Resource Group and Storage Account
```bash
az group create --name rg-app-dev --location eastus
az storage account create \
  --name stappdev001 \
  --resource-group rg-app-dev \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2
```

### Deploy an Azure Function App
```bash
az functionapp create \
  --resource-group rg-app-dev \
  --consumption-plan-location eastus \
  --runtime node \
  --runtime-version 20 \
  --functions-version 4 \
  --name my-func-app-dev \
  --storage-account stappdev001
```

### Deploy Bicep Template
```bash
az deployment group create \
  --resource-group rg-app-dev \
  --template-file main.bicep \
  --parameters environment=dev appName=myapp
```

## Common Patterns

### Bicep Baseline for App Service
```bicep
param location string = resourceGroup().location
param appName string

resource plan 'Microsoft.Web/serverfarms@2023-12-01' = {
  name: '${appName}-plan'
  location: location
  sku: {
    name: 'B1'
    tier: 'Basic'
  }
}

resource app 'Microsoft.Web/sites@2023-12-01' = {
  name: '${appName}-web'
  location: location
  properties: {
    serverFarmId: plan.id
    httpsOnly: true
  }
}
```

### Secure Secret Access with Managed Identity
```bash
# Assign system identity to web app
az webapp identity assign --name myapp-web --resource-group rg-app-dev

# Grant Key Vault secret read role
az role assignment create \
  --assignee <principal-id> \
  --role "Key Vault Secrets User" \
  --scope /subscriptions/<sub-id>/resourceGroups/rg-app-dev/providers/Microsoft.KeyVault/vaults/kv-app-dev
```

### Diagnostics and Monitoring Query
```kusto
AppRequests
| where TimeGenerated > ago(1h)
| summarize requests=count(), failures=countif(Success == false) by bin(TimeGenerated, 5m)
| order by TimeGenerated asc
```

## Best Practices

### Security
- Use managed identities instead of embedded secrets
- Apply least-privilege RBAC at resource-group scope or narrower
- Store secrets and certificates in Key Vault with access policies/RBAC
- Enforce policies with Azure Policy and Defender for Cloud recommendations

### Cost Optimization
- Right-size App Service plans, AKS node pools, and database tiers
- Use autoscaling for variable workloads
- Enable budget alerts and anomaly detection
- Clean up idle resources and old snapshots regularly

### Performance and Reliability
- Deploy across availability zones where required
- Use health probes, readiness checks, and retry patterns
- Front APIs with API Management/Application Gateway for resilience
- Monitor SLOs with Azure Monitor metrics and alert rules

### Operations
- Standardize naming conventions and tagging (`env`, `owner`, `costCenter`)
- Keep infrastructure definitions in Bicep/Terraform under version control
- Use staged deployments (dev/staging/prod) with gated approvals
- Run regular backup and restore drills for critical data services

## Troubleshooting

### Deployment Failures
- **AuthorizationFailed**: verify role assignments and scope
- **InvalidTemplateDeployment**: validate Bicep/ARM syntax and parameter values
- **QuotaExceeded**: check regional quotas and request increases if needed

### App Runtime Issues
- **Function cold start latency**: evaluate plan type and pre-warmed instances
- **App Service startup failures**: inspect container logs and app settings
- **AKS pod crash loops**: check probes, resource limits, and image tags

### Connectivity Problems
- **Storage/SQL access denied**: verify firewall rules, private endpoints, and identity permissions
- **DNS/VNet issues**: review private DNS zones, route tables, and NSGs
- **API errors**: inspect API Management policies and backend health

### Data and Monitoring Gaps
- **Missing telemetry**: verify Application Insights connection strings
- **No logs in workspace**: check diagnostic settings and destination workspace
- **Slow queries**: review indexes, DTU/vCore sizing, and query plans

## Integration Points

- **Azure CLI**: day-to-day provisioning and operations
- **IaC**: Bicep, ARM templates, Terraform AzureRM provider
- **CI/CD**: GitHub Actions, Azure DevOps Pipelines
- **Observability**: Azure Monitor, Application Insights, Log Analytics
- **Platform services**: Entra ID, Key Vault, API Management, Service Bus
