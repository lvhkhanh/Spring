---
name: bicep
description: '**WORKFLOW SKILL** — Create, refactor, validate, and deploy Azure Bicep infrastructure-as-code templates. USE FOR: authoring Bicep modules, Azure resource declarations, parameters, outputs, scopes, RBAC, deployment scripts, CI/CD deployment workflows, and ARM/Bicep troubleshooting. DO NOT USE FOR: non-Azure infrastructure, Terraform-only work, general Azure operations without infrastructure-as-code, or application code unrelated to Azure resources. INVOKES: file system tools for Bicep files, terminal for Azure CLI/Bicep commands, semantic search for existing IaC patterns.'
---

# Azure Bicep Skill

## Overview

This skill supports Azure infrastructure-as-code development with Bicep. It covers writing clean templates, composing reusable modules, validating deployments, handling environment parameters, and troubleshooting Azure Resource Manager deployment errors.

## Key Capabilities

### Template Authoring
- Create `main.bicep` files for resource-group, subscription, management-group, and tenant deployments
- Define parameters with types, defaults, decorators, and allowed values
- Declare Azure resources with stable names, locations, tags, identities, and dependencies
- Use outputs for IDs, endpoints, principal IDs, and integration values

### Module Design
- Split reusable infrastructure into `modules/*.bicep`
- Pass explicit parameters and outputs between modules
- Use clear module names and scoped deployments
- Avoid unnecessary coupling between unrelated resources

### Azure Resource Configuration
- Provision common Azure services such as App Service, Functions, Storage, Key Vault, SQL, VNet, Container Apps, AKS, Service Bus, and Log Analytics
- Configure managed identities, RBAC assignments, private endpoints, diagnostic settings, and locks
- Apply secure defaults for public network access, HTTPS-only settings, TLS versions, and secret handling
- Add standard tags for environment, owner, workload, cost center, and lifecycle

### Validation & Deployment
- Build and validate Bicep templates before deployment
- Use `what-if` to preview changes
- Deploy with Azure CLI at the correct scope
- Capture deployment outputs for downstream scripts and pipelines

### Troubleshooting
- Diagnose ARM validation errors, dependency cycles, invalid API versions, and property schema issues
- Resolve authorization, policy, quota, naming, and regional availability failures
- Inspect deployment operations when the top-level error is too generic
- Refactor templates when incremental changes become risky or duplicated

## Usage Examples

### Create a Resource Group Deployment
```
Create a Bicep template that deploys a Storage Account, Key Vault,
and Log Analytics workspace with secure defaults and environment tags.
```

### Modularize Existing Bicep
```
Refactor this large main.bicep into modules for networking,
monitoring, app hosting, and data resources.
```

### Debug Deployment Failure
```
This az deployment group create command failed with InvalidTemplate.
Find the likely Bicep issue and propose the smallest fix.
```

### Add CI/CD Deployment
```
Add a GitHub Actions workflow that validates Bicep, runs what-if,
and deploys to the dev resource group.
```

## Common Patterns

### Basic Bicep File
```bicep
targetScope = 'resourceGroup'

@description('Azure region for all regional resources.')
param location string = resourceGroup().location

@description('Deployment environment name.')
@allowed([
  'dev'
  'test'
  'prod'
])
param environment string

@description('Base workload name used in resource names.')
param workloadName string

var tags = {
  environment: environment
  workload: workloadName
  managedBy: 'bicep'
}
```

### Storage Account with Secure Defaults
```bicep
param storageAccountName string
param location string = resourceGroup().location
param tags object = {}

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  tags: tags
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    allowBlobPublicAccess: false
    allowSharedKeyAccess: false
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
  }
}

output storageAccountId string = storage.id
```

### Module Invocation
```bicep
module storageModule './modules/storage.bicep' = {
  name: 'storage-${environment}'
  params: {
    storageAccountName: storageAccountName
    location: location
    tags: tags
  }
}

output storageAccountId string = storageModule.outputs.storageAccountId
```

### Group Deployment Commands
```bash
az bicep build --file main.bicep

az deployment group what-if \
  --resource-group rg-app-dev \
  --template-file main.bicep \
  --parameters @parameters/dev.bicepparam

az deployment group create \
  --resource-group rg-app-dev \
  --template-file main.bicep \
  --parameters @parameters/dev.bicepparam
```

### Subscription Deployment Commands
```bash
az deployment sub what-if \
  --location eastus \
  --template-file main.bicep \
  --parameters @parameters/dev.bicepparam

az deployment sub create \
  --location eastus \
  --template-file main.bicep \
  --parameters @parameters/dev.bicepparam
```

## Best Practices

### Structure
- Keep `main.bicep` orchestration-focused and move reusable resources into modules
- Use `parameters/*.bicepparam` files for environment-specific values
- Keep names deterministic and compliant with each resource provider's naming rules
- Prefer symbolic dependencies over explicit `dependsOn` unless Azure cannot infer the dependency

### Security
- Use managed identities and role assignments instead of secrets where possible
- Store secrets in Key Vault and pass references, not secret values
- Disable public access when private networking is required
- Apply least-privilege RBAC at the narrowest practical scope

### Reliability
- Use current stable API versions supported in the target Azure cloud
- Validate location support for resource SKUs before deployment
- Use `what-if` before changes to shared or production environments
- Output values that later deployment stages need instead of recomputing them

### Maintainability
- Add descriptions to parameters and outputs that cross module boundaries
- Use consistent tag and naming conventions across modules
- Avoid embedding environment-specific constants in reusable modules
- Keep module interfaces small and explicit

## Troubleshooting

### Build or Lint Problems
- **BCP errors**: run `az bicep build --file <file>` and fix syntax, type, or symbol issues first
- **Unknown resource type**: verify the provider namespace, type path, and API version
- **Invalid property**: compare the property shape against the selected API version
- **Parameter mismatch**: check module parameter names, types, decorators, and required values

### Deployment Failures
- **AuthorizationFailed**: verify the deploying identity has permissions at the deployment scope and child scopes
- **InvalidTemplateDeployment**: inspect nested deployment operations for the actual resource-level error
- **RequestDisallowedByPolicy**: identify the Azure Policy assignment and adjust template values or request an exemption
- **QuotaExceeded**: check regional quota limits and target SKU availability
- **Conflict or AlreadyExists**: verify globally unique names and resource ownership

### Debug Commands
```bash
az deployment group show \
  --resource-group rg-app-dev \
  --name <deployment-name>

az deployment operation group list \
  --resource-group rg-app-dev \
  --name <deployment-name> \
  --query "[].{state:properties.provisioningState,type:properties.targetResource.resourceType,name:properties.targetResource.resourceName,error:properties.statusMessage.error.message}"
```

## Integration Points

- **Azure CLI**: `az bicep`, `az deployment group`, `az deployment sub`
- **Azure PowerShell**: `New-AzResourceGroupDeployment`, `New-AzSubscriptionDeployment`
- **CI/CD**: GitHub Actions, Azure DevOps Pipelines, deployment gates, environment approvals
- **Azure governance**: Azure Policy, RBAC, management groups, resource locks
- **Observability**: diagnostic settings, Log Analytics, Application Insights, Azure Monitor alerts
- **Security**: Managed identities, Key Vault, private endpoints, Defender for Cloud
