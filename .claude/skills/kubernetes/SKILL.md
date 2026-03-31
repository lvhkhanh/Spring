---
name: kubernetes
description: '**WORKFLOW SKILL** — Create, deploy, and manage Kubernetes applications and infrastructure. USE FOR: writing Kubernetes manifests, configuring deployments, managing services and ingress, implementing Helm charts, troubleshooting cluster issues, and optimizing resource usage. DO NOT USE FOR: non-Kubernetes container orchestration, infrastructure provisioning outside Kubernetes, or application code development. INVOKES: file system tools for manifest/chart creation/modification, terminal for kubectl commands, semantic search for Kubernetes patterns.'
---

# Kubernetes Development Skill

## Overview

This skill provides comprehensive support for Kubernetes application deployment and management, including manifest creation, resource configuration, service orchestration, and cluster operations. It focuses on best practices for container orchestration, scalability, and production readiness.

## Key Capabilities

### Manifest Creation & Management
- Write optimized Kubernetes manifests (Deployments, Services, ConfigMaps, Secrets)
- Create custom resource definitions and operators
- Implement resource limits, requests, and affinity rules
- Handle different workload types (Deployments, StatefulSets, DaemonSets, Jobs)

### Service Orchestration
- Configure Services, Ingress, and NetworkPolicies for traffic management
- Implement load balancing and service discovery
- Setup persistent volumes and storage classes
- Manage ConfigMaps and Secrets for configuration

### Helm Chart Development
- Create and maintain Helm charts for application packaging
- Implement chart templating and value management
- Handle chart dependencies and subcharts
- Develop reusable chart libraries and templates

### Cluster Operations & Troubleshooting
- Debug pod startup, networking, and resource issues
- Analyze cluster performance and resource utilization
- Implement monitoring and logging solutions
- Handle cluster upgrades and maintenance

### Security & Compliance
- Implement RBAC (Role-Based Access Control) policies
- Configure network policies and security contexts
- Manage secrets and sensitive data securely
- Implement pod security standards and admission controllers

## Usage Examples

### Complete Application Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app:latest
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: my-app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-app-service
            port:
              number: 80
```

### Helm Chart Structure
```yaml
# Chart.yaml
apiVersion: v2
name: my-app
description: A Helm chart for my application
type: application
version: 0.1.0
appVersion: "1.0.0"

# values.yaml
replicaCount: 3
image:
  repository: my-app
  tag: "latest"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  host: my-app.example.com

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "my-app.name" . }}
  template:
    metadata:
      labels:
        app: {{ include "my-app.name" . }}
    spec:
      containers:
      - name: app
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 8080
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
```

## Common Patterns

### Horizontal Pod Autoscaler
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

### ConfigMap for Environment Variables
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_URL: "postgresql://db:5432/myapp"
  REDIS_URL: "redis://redis:6379"
  LOG_LEVEL: "info"

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      containers:
      - name: app
        envFrom:
        - configMapRef:
            name: app-config
```

### RBAC Configuration
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: app-reader
rules:
- apiGroups: [""]
  resources: ["pods", "services"]
  verbs: ["get", "list", "watch"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-reader-binding
  namespace: default
subjects:
- kind: ServiceAccount
  name: app-service-account
  namespace: default
roleRef:
  kind: Role
  name: app-reader
  apiGroup: rbac.authorization.k8s.io
```

## Best Practices

### Resource Management
- Always set resource requests and limits for all containers
- Use appropriate resource classes for different workloads
- Implement pod disruption budgets for high availability
- Monitor resource usage and adjust allocations regularly

### Security
- Use non-root user for container execution
- Implement network policies to restrict pod communication
- Store sensitive data in Secrets, not ConfigMaps
- Regularly rotate service account tokens and certificates

### Networking
- Use Ingress controllers for external traffic management
- Implement proper service mesh for microservices communication
- Configure network policies for zero-trust networking
- Use appropriate service types based on use cases

### Observability
- Implement comprehensive logging and monitoring
- Use structured logging with consistent formats
- Setup distributed tracing for microservices
- Configure alerts for critical metrics and events

### Deployment Strategy
- Use rolling updates for zero-downtime deployments
- Implement blue-green or canary deployment patterns
- Setup proper health checks and readiness probes
- Maintain multiple environment configurations

## Troubleshooting

### Pod Issues
- **Pod Pending**: Check resource availability, node selectors, and affinity rules
- **Pod CrashLoopBackOff**: Examine container logs, resource limits, and health checks
- **Pod ImagePullBackOff**: Verify image registry access and image names/tags
- **Pod Evicted**: Check resource pressure and pod priority settings

### Service Issues
- **Service not accessible**: Verify selectors match pod labels and ports are correct
- **Load balancing not working**: Check service endpoints and readiness probes
- **DNS resolution failing**: Validate CoreDNS configuration and service names

### Networking Issues
- **Pods can't communicate**: Check network policies and security groups
- **External access failing**: Verify Ingress configuration and load balancer setup
- **Cross-namespace communication**: Ensure proper service accounts and permissions

### Performance Issues
- **High resource usage**: Analyze container metrics and adjust resource limits
- **Slow pod startup**: Optimize init containers and reduce image sizes
- **Network latency**: Check service mesh configuration and network policies

### Storage Issues
- **PVC pending**: Verify storage class availability and capacity
- **Volume mount failures**: Check volume permissions and mount paths
- **Data persistence problems**: Validate backup and recovery procedures

## Integration Points

### Development Tools
- **kubectl**: Command-line interface for cluster management
- **k9s**: Terminal-based UI for Kubernetes cluster management
- **Lens**: Desktop application for Kubernetes cluster management
- **VS Code Kubernetes extension**: IDE integration for manifest development

### Container Runtimes
- **Docker**: Primary container runtime for development
- **containerd**: Kubernetes-native container runtime
- **CRI-O**: Lightweight container runtime for Kubernetes

### Cloud Platforms
- **Amazon EKS**: Managed Kubernetes service on AWS
- **Google GKE**: Managed Kubernetes service on GCP
- **Azure AKS**: Managed Kubernetes service on Azure
- **DigitalOcean Kubernetes**: Managed Kubernetes service

### Monitoring & Observability
- **Prometheus**: Metrics collection and alerting
- **Grafana**: Visualization and dashboarding
- **ELK Stack**: Centralized logging solution
- **Jaeger**: Distributed tracing system

### CI/CD Tools
- **Jenkins**: Automation server with Kubernetes integration
- **GitLab CI**: Integrated CI/CD with Kubernetes deployment
- **ArgoCD**: GitOps continuous delivery for Kubernetes
- **Tekton**: Cloud-native CI/CD pipelines

### Service Mesh
- **Istio**: Service mesh for traffic management and security
- **Linkerd**: Lightweight service mesh for Kubernetes
- **Consul**: Service mesh with service discovery

### Storage Solutions
- **Persistent Volumes**: Kubernetes native storage abstraction
- **CSI Drivers**: Container Storage Interface implementations
- **Rook**: Cloud-native storage orchestrator
- **Longhorn**: Distributed block storage for Kubernetes