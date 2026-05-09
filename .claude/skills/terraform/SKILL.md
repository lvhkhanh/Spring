---
name: terraform
description: '**WORKFLOW SKILL** — Create, refactor, optimize, secure, and troubleshoot Terraform infrastructure-as-code configurations for multi-cloud environments. USE FOR: writing and organizing HCL modules, managing state, provisioning AWS/Azure/GCP/OCI resources, designing reusable module libraries, implementing CI/CD pipelines for infrastructure, migrating manual or legacy infrastructure to IaC, handling secrets and sensitive data, drift detection, cost optimization, and compliance enforcement. DO NOT USE FOR: application-level business logic, container orchestration internals (use Kubernetes skill), or database query tuning (use SQL skill). INVOKES: file system tools for HCL files and module scaffolding, terminal for terraform CLI commands, plan/apply analysis, state inspection, and provider documentation lookup.'
---

# Terraform Development Skill

## Overview

This skill provides comprehensive support for Terraform and infrastructure-as-code workloads across AWS, Azure, GCP, OCI, and hybrid environments. It helps author and refactor HCL configurations, design reusable modules, manage remote state safely, plan and apply changes with confidence, enforce security and compliance policies, optimize cloud costs, and migrate manual or legacy infrastructure into declarative, version-controlled Terraform code.

## Key Capabilities

### HCL Authoring
- Create resource, data source, variable, output, and local blocks with idiomatic HCL
- Build conditional logic with `count`, `for_each`, and dynamic blocks
- Use expressions, functions, and type constraints for clean, readable configurations
- Write provider configurations with version pinning and alias support

### Module Design
- Design reusable modules with clear input variables, outputs, and documentation
- Structure root modules, child modules, and shared module libraries
- Implement module composition patterns for layered architectures
- Version modules with semantic versioning and publish to registries

### State Management
- Configure remote backends (S3, GCS, Azure Blob, Terraform Cloud, PostgreSQL)
- Handle state locking, encryption, and access control
- Perform state operations: import, move, remove, taint, untaint, replace
- Recover from state corruption, split monolithic state, and migrate backends

### Planning and Applying
- Analyze `terraform plan` output for expected vs unexpected changes
- Implement targeted applies, resource replacement, and refresh-only plans
- Design approval workflows with plan file artifacts
- Handle destroy operations safely with dependency awareness

### Security and Compliance
- Manage secrets with environment variables, vault integration, or sensitive variable marking
- Implement least-privilege IAM roles for Terraform execution
- Use policy-as-code with Sentinel, OPA, or tflint rules
- Enforce tagging, encryption, network isolation, and naming standards

### Multi-Cloud and Provider Management
- Configure multiple providers, regions, and accounts in a single configuration
- Handle provider authentication across AWS, Azure, GCP, and OCI
- Manage provider version constraints and upgrade paths
- Use terraform_remote_state and data sources for cross-stack references

### CI/CD Integration
- Design pipeline stages: validate, plan, approve, apply
- Implement automated drift detection and remediation
- Configure branch-based workflows with environment promotion
- Integrate with GitHub Actions, GitLab CI, Azure DevOps, Jenkins, and Terraform Cloud

### Migration and Import
- Import existing cloud resources into Terraform state
- Generate configuration from imported resources
- Plan incremental migration from manual infrastructure to IaC
- Handle resource adoption without downtime or recreation

## Usage Examples

### Provision a VPC with subnets
```
Create an AWS VPC with public and private subnets across 3 AZs, NAT gateways, and route tables using a reusable module.
```

### Create a reusable module
```
Design a Terraform module for an RDS PostgreSQL instance with parameter groups, subnet groups, security groups, and automated backups.
```

### Import existing infrastructure
```
Import an existing AWS S3 bucket and its associated IAM policies into Terraform state and generate the matching HCL configuration.
```

### Migrate to remote state
```
Migrate local Terraform state to an S3 backend with DynamoDB locking, encryption, and versioning.
```

### Multi-environment setup
```
Structure Terraform code for dev, staging, and production environments using workspaces or directory-based separation with shared modules.
```

### Cost optimization review
```
Review this Terraform configuration and suggest resource right-sizing, reserved capacity, and architecture changes to reduce cloud spend.
```

### Security hardening
```
Audit this Terraform code for security issues: overly permissive IAM, unencrypted storage, public network exposure, and missing logging.
```

## Common Patterns

### Provider configuration with version pinning
```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "environments/production/terraform.tfstate"
    region         = "ap-southeast-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "terraform"
      Project     = var.project_name
    }
  }
}
```

### Variable definitions with validation
```hcl
variable "environment" {
  description = "Deployment environment name"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "production"], var.environment)
    error_message = "Environment must be dev, staging, or production."
  }
}

variable "instance_type" {
  description = "EC2 instance type for the application servers"
  type        = string
  default     = "t3.medium"

  validation {
    condition     = can(regex("^t3\\.", var.instance_type))
    error_message = "Only t3 instance types are allowed."
  }
}

variable "tags" {
  description = "Additional tags to apply to all resources"
  type        = map(string)
  default     = {}
}
```

### Reusable module structure
```
modules/
  vpc/
    main.tf          # Resource definitions
    variables.tf     # Input variables
    outputs.tf       # Output values
    versions.tf      # Provider and terraform version constraints
    README.md        # Module documentation
    examples/
      basic/
        main.tf      # Example usage
```

```hcl
# modules/vpc/main.tf
resource "aws_vpc" "this" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-vpc"
  })
}

resource "aws_subnet" "private" {
  for_each = { for idx, az in var.availability_zones : az => idx }

  vpc_id            = aws_vpc.this.id
  cidr_block        = cidrsubnet(var.cidr_block, 8, each.value)
  availability_zone = each.key

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-private-${each.key}"
    Tier = "private"
  })
}

resource "aws_subnet" "public" {
  for_each = { for idx, az in var.availability_zones : az => idx }

  vpc_id                  = aws_vpc.this.id
  cidr_block              = cidrsubnet(var.cidr_block, 8, each.value + 100)
  availability_zone       = each.key
  map_public_ip_on_launch = true

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-public-${each.key}"
    Tier = "public"
  })
}
```

```hcl
# modules/vpc/outputs.tf
output "vpc_id" {
  description = "ID of the created VPC"
  value       = aws_vpc.this.id
}

output "private_subnet_ids" {
  description = "IDs of private subnets"
  value       = [for s in aws_subnet.private : s.id]
}

output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = [for s in aws_subnet.public : s.id]
}
```

### for_each with complex objects
```hcl
variable "s3_buckets" {
  description = "Map of S3 buckets to create"
  type = map(object({
    versioning    = bool
    force_destroy = bool
    lifecycle_rules = list(object({
      prefix                = string
      expiration_days       = number
      transition_storage    = optional(string, "GLACIER")
      transition_days       = optional(number, 90)
    }))
  }))
}

resource "aws_s3_bucket" "this" {
  for_each = var.s3_buckets

  bucket        = "${var.project_name}-${var.environment}-${each.key}"
  force_destroy = each.value.force_destroy

  tags = merge(var.tags, {
    Name = each.key
  })
}

resource "aws_s3_bucket_versioning" "this" {
  for_each = { for k, v in var.s3_buckets : k => v if v.versioning }

  bucket = aws_s3_bucket.this[each.key].id
  versioning_configuration {
    status = "Enabled"
  }
}
```

### Dynamic blocks for repeated nested configuration
```hcl
resource "aws_security_group" "this" {
  name_prefix = "${var.project_name}-${var.environment}-"
  vpc_id      = var.vpc_id

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      description     = ingress.value.description
      from_port       = ingress.value.from_port
      to_port         = ingress.value.to_port
      protocol        = ingress.value.protocol
      cidr_blocks     = ingress.value.cidr_blocks
      security_groups = ingress.value.security_groups
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  lifecycle {
    create_before_destroy = true
  }
}
```

### Conditional resource creation
```hcl
resource "aws_nat_gateway" "this" {
  count = var.enable_nat_gateway ? length(var.availability_zones) : 0

  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[var.availability_zones[count.index]].id

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-nat-${count.index}"
  })

  depends_on = [aws_internet_gateway.this]
}
```

### Remote state data source for cross-stack references
```hcl
data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    bucket = "company-terraform-state"
    key    = "environments/${var.environment}/vpc/terraform.tfstate"
    region = var.aws_region
  }
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.app.id
  instance_type = var.instance_type
  subnet_id     = data.terraform_remote_state.vpc.outputs.private_subnet_ids[0]
}
```

### Lifecycle rules for safe resource management
```hcl
resource "aws_db_instance" "this" {
  identifier     = "${var.project_name}-${var.environment}"
  engine         = "postgres"
  engine_version = var.engine_version
  instance_class = var.instance_class

  allocated_storage     = var.allocated_storage
  max_allocated_storage = var.max_allocated_storage
  storage_encrypted     = true

  db_name  = var.database_name
  username = var.master_username
  password = var.master_password

  multi_az               = var.environment == "production"
  backup_retention_period = var.environment == "production" ? 30 : 7
  deletion_protection     = var.environment == "production"

  vpc_security_group_ids = [aws_security_group.db.id]
  db_subnet_group_name   = aws_db_subnet_group.this.name

  lifecycle {
    prevent_destroy = true
    ignore_changes  = [password]
  }
}
```

### Sensitive variable handling
```hcl
variable "master_password" {
  description = "Master password for the database"
  type        = string
  sensitive   = true

  validation {
    condition     = length(var.master_password) >= 16
    error_message = "Master password must be at least 16 characters."
  }
}

# Never output sensitive values in plain text
output "db_endpoint" {
  description = "Database endpoint"
  value       = aws_db_instance.this.endpoint
}

output "db_password_secret_arn" {
  description = "ARN of the secret containing the database password"
  value       = aws_secretsmanager_secret.db_password.arn
}
```

### Moved blocks for refactoring without recreation
```hcl
# When renaming a resource or moving into/out of a module
moved {
  from = aws_instance.web_server
  to   = aws_instance.application
}

moved {
  from = aws_security_group.web
  to   = module.networking.aws_security_group.application
}
```

### Import blocks for adopting existing resources
```hcl
import {
  to = aws_s3_bucket.legacy_data
  id = "my-existing-bucket-name"
}

resource "aws_s3_bucket" "legacy_data" {
  bucket = "my-existing-bucket-name"

  tags = {
    Name        = "legacy-data"
    ManagedBy   = "terraform"
    ImportedOn  = "2025-01-15"
  }
}
```

### Local values for computed expressions
```hcl
locals {
  common_tags = merge(var.tags, {
    Environment = var.environment
    ManagedBy   = "terraform"
    Project     = var.project_name
    Region      = var.aws_region
  })

  is_production = var.environment == "production"

  subnet_cidrs = {
    for idx, az in var.availability_zones :
    az => {
      private = cidrsubnet(var.cidr_block, 8, idx)
      public  = cidrsubnet(var.cidr_block, 8, idx + 100)
    }
  }
}
```

## Project Structure Guidance

### Small project (single environment)
```
project/
  main.tf
  variables.tf
  outputs.tf
  versions.tf
  terraform.tfvars
```

### Medium project (multiple environments, shared modules)
```
project/
  modules/
    vpc/
    rds/
    ecs/
  environments/
    dev/
      main.tf
      variables.tf
      terraform.tfvars
      backend.tf
    staging/
    production/
```

### Large project (multi-team, multi-account)
```
infrastructure/
  modules/                    # Shared module library
    networking/
    compute/
    database/
    security/
  stacks/                     # Independent state files per stack
    networking/
      environments/
        dev/
        production/
    application/
      environments/
        dev/
        production/
    data/
      environments/
        dev/
        production/
  policies/                   # Sentinel or OPA policies
  scripts/                    # Helper scripts for CI/CD
```

### File naming conventions
- `main.tf` — primary resource definitions
- `variables.tf` — input variable declarations
- `outputs.tf` — output value declarations
- `versions.tf` — terraform and provider version constraints
- `backend.tf` — backend configuration (if not in versions.tf)
- `locals.tf` — local value definitions
- `data.tf` — data source definitions
- `providers.tf` — provider configurations (for multi-provider setups)

## Best Practices

### General
- Pin provider and Terraform versions to avoid unexpected breaking changes
- Use `terraform fmt` and `terraform validate` before every commit
- Run `tflint` or equivalent linter for provider-specific best practices
- Keep resource names descriptive and consistent: `aws_instance.app_server`, not `aws_instance.this`
- Use `locals` for repeated expressions instead of duplicating logic across resources
- Prefer `for_each` over `count` for resources that have a natural key to avoid index-shift problems
- Never hardcode secrets, credentials, or account IDs in HCL files

### State management
- Always use remote state with locking for team environments
- Enable state encryption at rest and restrict backend access with IAM
- Never edit state files manually — use `terraform state` commands
- Split large monolithic state into smaller stacks by blast radius and team ownership
- Use `terraform_remote_state` data sources for cross-stack references
- Back up state files and enable versioning on the state bucket

### Module design
- Keep modules focused on a single logical component
- Expose only necessary variables; use sensible defaults for optional ones
- Always include `description` on variables and outputs
- Use `validation` blocks for input constraints
- Version modules with semantic versioning and document breaking changes
- Include examples and README.md in every module
- Avoid deep module nesting (max 2–3 levels)

### Security
- Mark sensitive variables and outputs with `sensitive = true`
- Use IAM roles with least privilege for Terraform execution
- Store secrets in vault or secrets manager, reference via data sources
- Enable encryption for all storage and transit resources by default
- Restrict security group rules — avoid `0.0.0.0/0` for ingress
- Use `checkov`, `tfsec`, or Sentinel for automated security scanning
- Audit who can run `terraform apply` in production

### Lifecycle and safety
- Use `prevent_destroy` on critical resources (databases, state buckets)
- Use `create_before_destroy` for zero-downtime replacements
- Use `ignore_changes` for attributes managed outside Terraform (auto-scaling, external config)
- Use `moved` blocks when refactoring to avoid resource recreation
- Always review `terraform plan` output before applying
- Use `-target` sparingly — it bypasses dependency resolution

### CI/CD
- Separate plan and apply into distinct pipeline stages with manual approval
- Store plan output as an artifact and apply the exact saved plan
- Run `terraform plan` on pull requests for change visibility
- Use workspace or directory isolation per environment
- Implement drift detection on a schedule
- Tag every apply with commit SHA, pipeline ID, and operator

### Cost awareness
- Use `infracost` or similar tools to estimate cost impact before applying
- Default to smaller instance types; right-size after monitoring
- Use auto-scaling, spot instances, and reserved capacity where appropriate
- Set up billing alerts and budget constraints per environment
- Review and clean up unused resources regularly

## Troubleshooting

### Initialization and providers
- `Error: Failed to query available provider packages`: check network access, registry URL, and provider version constraints
- `Error: Unsupported Terraform Core version`: upgrade Terraform or relax `required_version`
- `Error: Duplicate provider configuration`: remove duplicate provider blocks or use aliases

### State issues
- `Error: Error acquiring the state lock`: another process holds the lock — check running pipelines, then force-unlock only if certain
- `Error: state snapshot was created by Terraform vX.Y`: upgrade Terraform or use the matching version
- Resource exists in cloud but not in state: use `terraform import` to adopt it
- Resource in state but deleted from cloud: use `terraform state rm` then re-plan
- State file corruption: restore from versioned backup in the state bucket

### Planning and applying
- `Error: Cycle detected`: break circular dependencies with `depends_on` or restructure resources
- Unexpected resource recreation on plan: check if a ForceNew attribute changed (instance type, subnet, AMI)
- `Error: Provider produced inconsistent result`: provider bug — pin to a stable version or report upstream
- Drift detected on every plan: use `ignore_changes` for externally managed attributes
- `-target` creates partial state: follow up with a full plan/apply to reconcile

### Module and variable issues
- `Error: Unsupported argument`: variable not declared in module — check `variables.tf`
- `Error: Invalid value for variable`: validation constraint failed — review the validation block
- Module outputs not available: ensure `output` blocks exist and the module is referenced correctly
- `Error: Module not installed`: run `terraform init` or `terraform get`

### Authentication and permissions
- `Error: NoCredentialProviders`: set AWS credentials via environment, profile, or IAM role
- `Error: AuthorizationError`: the executing role lacks permissions — check IAM policy
- Cross-account access denied: verify assume-role configuration and trust policies
- Provider-specific auth: check `ARM_*` (Azure), `GOOGLE_*` (GCP), `TF_VAR_*` environment variables

### Resource-specific
- S3 bucket deletion fails: enable `force_destroy` or empty the bucket first
- RDS deletion blocked: disable `deletion_protection` before destroy
- Security group deletion fails: dependent ENIs still exist — remove attachments first
- VPC deletion fails: dependent resources (subnets, gateways, endpoints) must be destroyed first
- Timeout on resource creation: increase `timeouts` block or check cloud service health

## Integration Points

- Cloud providers: AWS, Azure, GCP, OCI, Alibaba Cloud, VMware vSphere
- State backends: S3, GCS, Azure Blob, Terraform Cloud, Consul, PostgreSQL
- Secret management: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager
- CI/CD: GitHub Actions, GitLab CI, Azure DevOps, Jenkins, Spacelift, Terraform Cloud
- Policy: Sentinel, OPA (Open Policy Agent), Checkov, tfsec, tflint
- Cost: Infracost, AWS Cost Explorer, Azure Cost Management
- Monitoring: CloudWatch, Datadog, Prometheus (for infrastructure metrics)
- Orchestration: Terragrunt (multi-module orchestration), Atlantis (PR-based workflow)
- Version control: Git with branch protection, PR-based reviews, and tagged releases
