---
name: sa
description: '**WORKFLOW SKILL** — Design, document, and implement software architecture patterns and principles. USE FOR: system design, architectural patterns, component design, scalability planning, technology selection, architectural documentation. DO NOT USE FOR: low-level coding, debugging, or infrastructure provisioning. INVOKES: file system tools for documentation creation, semantic search for pattern discovery, terminal for diagram generation.'
---

# Software Architecture Skill

## Overview

This skill provides comprehensive support for software architecture design, documentation, and implementation guidance. It covers architectural patterns, system design principles, scalability planning, and technology selection to create robust, maintainable software systems.

## Key Capabilities

### System Design & Analysis
- Analyze requirements and design high-level system architecture
- Create component diagrams, sequence diagrams, and deployment views
- Design microservices, monolithic, and hybrid architectures
- Plan for scalability, reliability, and performance requirements

### Architectural Patterns
- Implement MVC, MVVM, layered, hexagonal, and CQRS patterns
- Design event-driven, message-based, and reactive architectures
- Apply domain-driven design (DDD) principles and bounded contexts
- Create clean architecture with proper separation of concerns

### Technology Selection & Evaluation
- Evaluate and recommend technology stacks for specific use cases
- Design data storage strategies (SQL, NoSQL, caching, search)
- Plan integration patterns (APIs, messaging, streaming)
- Assess cloud-native vs traditional deployment options

### Documentation & Communication
- Create architectural decision records (ADRs) and design documents
- Document APIs, data flows, and system interactions
- Generate technical specifications and implementation guides
- Create diagrams using PlantUML, Mermaid, or draw.io formats

### Quality Attributes & Non-Functional Requirements
- Design for security, performance, and maintainability
- Implement monitoring, logging, and observability patterns
- Plan for disaster recovery and business continuity
- Address compliance and regulatory requirements

## Usage Examples

### System Architecture Design
```
Design a scalable e-commerce platform that can handle 10,000 concurrent users, with microservices architecture, event-driven communication, and multi-region deployment.
```

### Architectural Pattern Implementation
```
Implement CQRS pattern for a banking system with separate read and write models, event sourcing for audit trails, and eventual consistency.
```

### Technology Stack Recommendation
```
Recommend technology stack for a real-time analytics platform processing 1M events/second with sub-second latency requirements.
```

## Common Patterns

### Microservices Architecture
```yaml
# Service decomposition example
services:
  - user-service: User management and authentication
  - order-service: Order processing and inventory
  - payment-service: Payment processing and fraud detection
  - notification-service: Email/SMS notifications
  - api-gateway: Request routing and rate limiting
```

### Event-Driven Architecture
```javascript
// Event sourcing pattern
class OrderAggregate {
  constructor() {
    this.events = [];
  }
  
  createOrder(orderData) {
    const event = new OrderCreatedEvent(orderData);
    this.apply(event);
    this.events.push(event);
  }
  
  apply(event) {
    // Apply event to aggregate state
  }
}
```

### Clean Architecture Layers
```
┌─────────────────────────────────────┐
│        Presentation Layer           │
│  (Controllers, Views, DTOs)         │
├─────────────────────────────────────┤
│        Application Layer            │
│  (Use Cases, Commands, Queries)     │
├─────────────────────────────────────┤
│        Domain Layer                 │
│  (Entities, Value Objects, Domain   │
│   Services, Domain Events)          │
├─────────────────────────────────────┤
│        Infrastructure Layer         │
│  (Repositories, External APIs,      │
│   Frameworks, Databases)            │
└─────────────────────────────────────┘
```

## Best Practices

### Design Principles
- **SOLID Principles**: Single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion
- **DRY (Don't Repeat Yourself)**: Eliminate code duplication through abstraction
- **KISS (Keep It Simple Stupid)**: Prefer simple solutions over complex ones
- **YAGNI (You Aren't Gonna Need It)**: Don't implement features until they're needed

### Scalability Planning
- **Horizontal vs Vertical Scaling**: Choose based on application characteristics
- **Database Sharding**: Plan for data distribution and query routing
- **Caching Strategies**: Implement multi-level caching (browser, CDN, application, database)
- **Load Balancing**: Design for traffic distribution and failover

### Security Architecture
- **Defense in Depth**: Multiple security layers and controls
- **Zero Trust Model**: Never trust, always verify
- **Secure by Design**: Security considerations in every design decision
- **Privacy by Design**: Data protection and compliance from the start

### Documentation Standards
- **Living Documentation**: Keep documentation current with code changes
- **Multiple Audiences**: Technical docs for developers, business docs for stakeholders
- **Diagrams as Code**: Use text-based diagram formats for version control
- **API Documentation**: Comprehensive OpenAPI/Swagger specifications

## Troubleshooting

### Common Architectural Issues
- **Tight Coupling**: Break dependencies with interfaces and dependency injection
- **God Classes**: Decompose large classes into smaller, focused components
- **Circular Dependencies**: Restructure packages and modules to eliminate cycles
- **Performance Bottlenecks**: Identify and optimize critical paths

### Scalability Problems
- **Database Connection Pooling**: Configure appropriate pool sizes
- **Memory Leaks**: Implement proper resource management and monitoring
- **Thread Contention**: Use async patterns and connection pooling
- **Cache Invalidation**: Implement cache-aside, write-through, or write-behind patterns

### Integration Challenges
- **API Versioning**: Use semantic versioning and backward compatibility
- **Data Consistency**: Implement saga patterns for distributed transactions
- **Error Handling**: Design comprehensive error handling and retry mechanisms
- **Monitoring Gaps**: Implement distributed tracing and centralized logging

### Technology Selection Mistakes
- **Over-Engineering**: Choose appropriate technology complexity for the problem
- **Vendor Lock-in**: Design for portability and migration paths
- **Skill Gaps**: Assess team capabilities and training requirements
- **Cost Optimization**: Balance development speed with operational costs

## Integration Points

### Development Tools
- **IDE Integration**: Architecture plugins for IntelliJ, VS Code
- **Modeling Tools**: Enterprise Architect, Sparx EA, Visual Paradigm
- **Documentation Platforms**: Confluence, Notion, GitBook
- **Version Control**: Git with architectural decision records

### Cloud Platforms
- **AWS**: ECS, Lambda, API Gateway, CloudFormation
- **Azure**: AKS, Functions, API Management, ARM templates
- **GCP**: Cloud Run, Cloud Functions, API Gateway, Deployment Manager
- **Multi-Cloud**: Design for cloud portability and hybrid deployments

### Frameworks & Libraries
- **Spring Boot**: Microservices, reactive programming, cloud integration
- **.NET Core**: Clean architecture, dependency injection, middleware
- **Node.js**: Event-driven architecture, microservices, serverless
- **Python**: Django/Flask for web, FastAPI for APIs, Celery for async tasks

### Data & Storage
- **Relational Databases**: PostgreSQL, MySQL, SQL Server for transactional data
- **NoSQL Databases**: MongoDB, Cassandra, DynamoDB for flexible schemas
- **Search Engines**: Elasticsearch, Solr for full-text search
- **Caching**: Redis, Memcached for performance optimization

### DevOps & Deployment
- **Container Orchestration**: Kubernetes, Docker Swarm, ECS
- **CI/CD Pipelines**: Jenkins, GitLab CI, GitHub Actions
- **Infrastructure as Code**: Terraform, CloudFormation, Ansible
- **Monitoring**: Prometheus, Grafana, ELK stack, New Relic