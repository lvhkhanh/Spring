---
name: gcp
description: '**WORKFLOW SKILL** — Create, deploy, and manage Google Cloud Platform applications and infrastructure. USE FOR: GCP service configuration, Cloud Functions/Run deployment, BigQuery data analysis, Cloud Storage operations, IAM management, and infrastructure as code. DO NOT USE FOR: non-GCP cloud platforms, general programming, or local development. INVOKES: terminal for gcloud commands, file system tools for configuration files, semantic search for GCP patterns.'
---

# Google Cloud Platform Development Skill

## Overview

This skill provides comprehensive support for Google Cloud Platform development, deployment, and operations. It covers infrastructure as code, serverless computing, data analytics, and cloud-native application development with best practices for scalability, security, and cost optimization.

## Key Capabilities

### Infrastructure as Code
- Deploy Cloud Run services, Cloud Functions, and App Engine applications
- Configure Cloud Storage buckets, BigQuery datasets, and Pub/Sub topics
- Set up VPC networks, subnets, and firewall rules
- Manage IAM roles, service accounts, and permissions

### Application Development
- Build serverless applications with Cloud Functions and Cloud Run
- Create data pipelines with Dataflow and Cloud Composer
- Implement microservices with Cloud Run and API Gateway
- Develop ML models with Vertex AI and BigQuery ML

### Data & Analytics
- Design BigQuery schemas and optimize queries
- Build data pipelines with Dataflow and Pub/Sub
- Create dashboards with Looker Studio and Data Studio
- Implement real-time analytics with Bigtable and Spanner

### DevOps & Operations
- Set up CI/CD pipelines with Cloud Build
- Configure monitoring with Cloud Monitoring and Logging
- Implement security with Cloud Armor and Identity-Aware Proxy
- Manage costs with billing alerts and budget controls

## Usage Examples

### Deploy Cloud Function
```bash
# Deploy a Python Cloud Function
gcloud functions deploy my-function \
  --runtime python39 \
  --trigger-http \
  --allow-unauthenticated \
  --source . \
  --entry-point hello_world
```

### Create BigQuery Dataset
```sql
-- Create dataset and table
CREATE SCHEMA `my-project.my_dataset`;
CREATE TABLE `my-project.my_dataset.users` (
  user_id INT64,
  name STRING,
  email STRING,
  created_at TIMESTAMP
);
```

### Cloud Run Service
```yaml
# cloud-run-service.yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: my-service
spec:
  template:
    spec:
      containers:
      - image: gcr.io/my-project/my-service:latest
        ports:
        - containerPort: 8080
```

## Common Patterns

### Serverless Function Structure
```python
import functions_framework
from google.cloud import firestore

@functions_framework.http
def process_data(request):
    """Process incoming data and store in Firestore."""
    db = firestore.Client()
    
    # Parse request data
    data = request.get_json()
    
    # Process and validate
    processed_data = validate_and_transform(data)
    
    # Store in Firestore
    doc_ref = db.collection('processed_data').document()
    doc_ref.set(processed_data)
    
    return {'status': 'success', 'id': doc_ref.id}
```

### Infrastructure Deployment
```terraform
# main.tf
resource "google_cloud_run_service" "api" {
  name     = "my-api"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "gcr.io/my-project/my-api:latest"
        ports {
          container_port = 8080
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}
```

### BigQuery Optimization
```sql
-- Optimized query with partitioning
SELECT
  user_id,
  COUNT(*) as order_count,
  SUM(amount) as total_amount
FROM `my-project.ecommerce.orders`
WHERE DATE(created_at) >= '2024-01-01'
  AND status = 'completed'
GROUP BY user_id
ORDER BY total_amount DESC
LIMIT 100
```

## Best Practices

### Security & Compliance
- Use least privilege IAM roles and service accounts
- Enable VPC Service Controls for data protection
- Implement Cloud Armor for DDoS protection
- Use Cloud KMS for encryption key management
- Enable audit logging for compliance

### Cost Optimization
- Use committed use discounts for predictable workloads
- Implement autoscaling for variable traffic
- Choose appropriate machine types and regions
- Set up budget alerts and cost monitoring
- Use preemptible VMs for batch processing

### Performance & Reliability
- Implement global load balancing for high availability
- Use Cloud CDN for static content delivery
- Configure health checks and auto-healing
- Set up proper monitoring and alerting
- Use Cloud Trace for performance debugging

### Development Workflow
- Use Cloud Source Repositories for version control
- Implement CI/CD with Cloud Build
- Use Cloud Deploy for progressive rollouts
- Enable canary deployments for testing
- Implement feature flags for gradual releases

## Troubleshooting

### Common Deployment Issues
- **Permission Denied**: Check IAM roles and service account permissions
- **Quota Exceeded**: Review resource quotas and request increases
- **Timeout Errors**: Increase function timeout or optimize code
- **Cold Start Issues**: Use Cloud Run for faster startups

### Data Pipeline Problems
- **BigQuery Job Failures**: Check query syntax and resource allocation
- **Dataflow Pipeline Stuck**: Verify worker configuration and network access
- **Pub/Sub Message Loss**: Confirm subscription settings and ack deadlines

### Performance Issues
- **High Latency**: Check region selection and CDN configuration
- **Memory Leaks**: Monitor Cloud Monitoring metrics and logs
- **Database Slow Queries**: Use BigQuery query plans and optimization

### Cost Issues
- **Unexpected Bills**: Review billing reports and resource usage
- **Idle Resources**: Set up auto-shutdown for development environments
- **Storage Costs**: Implement lifecycle policies for Cloud Storage

## Integration Points

### Development Tools
- **VS Code**: Cloud Code extension for GCP development
- **IntelliJ IDEA**: Google Cloud Tools plugin
- **Terraform**: Infrastructure as code for GCP resources
- **Docker**: Containerization for Cloud Run deployments

### GCP Services Ecosystem
- **Firebase**: Mobile and web app development
- **Google Workspace**: Integration with enterprise tools
- **Anthos**: Multi-cloud and hybrid deployments
- **Apigee**: API management and monetization

### Third-Party Integrations
- **GitHub Actions**: CI/CD workflows for GCP
- **Jenkins**: Enterprise CI/CD pipelines
- **Prometheus**: Custom monitoring and alerting
- **Grafana**: Advanced dashboards and visualization

### Data Sources
- **Google Analytics**: Web and app analytics data
- **Google Ads**: Marketing campaign data
- **YouTube Analytics**: Content performance metrics
- **Google Play**: Mobile app analytics