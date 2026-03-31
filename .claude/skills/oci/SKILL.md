---
name: oci
description: "**WORKFLOW SKILL** — Design, deploy, and manage applications and infrastructure on Oracle Cloud Infrastructure (OCI). USE FOR: provisioning compute and storage, setting up networking, building secure cloud-native applications, and operating OCI services. DO NOT USE FOR: non-OCI clouds, on-prem only systems. INVOKES: terminal commands for OCI CLI, scripting, API references, security best practices, and deployment patterns."
---

# Oracle Cloud Infrastructure (OCI) Skill

## Overview

This skill focuses on Oracle Cloud Infrastructure (OCI) operations and developer workflows. It helps with architecture design, service selection, deployment patterns, and operational handling for OCI including compute, networking, storage, databases, security, and automation.

## Key Capabilities

- Provisioning OCI resources using CLI, Terraform, and SDKs
- Designing secure network topologies with VCNs, subnets, NSGs, and route tables
- Managing compute instances (VMs, bare metal, functions, containers)
- Configuring object storage, block volumes, file storage, and archive tiers
- Implementing database services (Autonomous DB, MySQL, Oracle DB, Exadata)
- Using Identity and Access Management (IAM) policies and compartment strategies
- Deploying infrastructure-as-code and automation (Terraform, Cloud Shell, Resource Manager)
- Monitoring, logging, and alerting with OCI Monitoring, Logging, and Events
- Applying cost controls with budgets, tagging, and lifecycle rules

## Usage Examples

### Create a VCN and subnet (OCI CLI)

```bash
oci network vcn create --compartment-id $COMPARTMENT_OCID --display-name "app-vcn" --cidr-block "10.0.0.0/16"
VCN_OCID=$(oci network vcn list --compartment-id $COMPARTMENT_OCID --display-name "app-vcn" --query 'data[0].id' --raw-output)
oci network subnet create --compartment-id $COMPARTMENT_OCID --vcn-id $VCN_OCID --display-name "app-subnet" --cidr-block "10.0.1.0/24" --dns-label "appsub" --prohibit-public-ip-on-vnic true
```

### Deploy a Compute instance via Terraform

```hcl
provider "oci" {
  tenancy_ocid    = var.tenancy_ocid
  user_ocid       = var.user_ocid
  fingerprint     = var.fingerprint
  private_key_path = var.private_key_path
  region          = var.region
}

resource "oci_core_instance" "app" {
  compartment_id = var.compartment_ocid
  availability_domain = var.availability_domain
  shape = "VM.Standard.E3.Flex"
  source_details {
    source_type = "image"
    image_id = var.image_id
  }
  metadata = {
    ssh_authorized_keys = file(var.ssh_public_key_path)
  }
}
```

### Configure IAM policy

```text
Allow group Developers to manage virtual-network-family in compartment App
Allow group Developers to manage compute-family in compartment App
Allow group Developers to use object-family in compartment App
```

## Common Patterns

- Use compartments to isolate environments (dev/test/prod) and apply least privilege policies.
- Standardize tags for ownership, environment, application and cost center before resource creation.
- Build immutable infrastructure with Terraform + Object Storage for state, and use `oci_resource_manager_stack`.
- Create pre-authenticated requests for time-bound object storage access in data pipelines.
- Protect databases with DB tools, backup policies and data safe scanning.

## Best Practices

- Always secure credentials and use instance principals where possible.
- Enable and enforce KMS encryption for storage volumes and object buckets.
- Use Service Gateway for private object storage access and NAT Gateway for internet-bound traffic as needed.
- Centralize logging using OCI Logging and forward to OCI Logging Analytics / external SIEM.
- Test disaster recovery with DR zones and cross-region replication for critical workloads.

## Troubleshooting

- `InvalidCredentials` / `NotAuthorizedOrNotFound` in CLI: validate `oci setup config`, user policy, and compartment IDs.
- Slow startup on instances: review shape, image, boot volume size, cloud-init scripts, and OS metrics.
- Networking issues: verify security lists, NSGs, route table entries, and DNS zones in OCI.
- Terraform state conflicts: lock the state in Object Storage bucket using RDS and Terraform locking.
- DB connection problems: check network rules, IPC rules, connection strings, wallet configuration, and local firewall.

## Integration Points

- OCI CLI and SDKs for Python, Java, Go, Node.js.
- Terraform + OCI Resource Manager for repeatable infrastructure deployments.
- Oracle Cloud Observability and Management for metrics, logs, events, and alarms.
- OCI DevOps for CI/CD pipelines and release automation.
- Cloud Shell and local shell automation for scripted operational tasks.
