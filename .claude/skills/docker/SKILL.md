---
name: docker
description: '**WORKFLOW SKILL** — Create, manage, and optimize Docker containers and images. USE FOR: building Docker images, writing Dockerfiles, creating docker-compose files, container orchestration, debugging container issues, and implementing container best practices. DO NOT USE FOR: non-container development, infrastructure provisioning, or application code development. INVOKES: file system tools for Dockerfile/docker-compose creation/modification, terminal for Docker commands, semantic search for container patterns.'
---

# Docker Development Skill

## Overview

This skill provides complete support for Docker container development, including image creation, container management, orchestration, and deployment. It focuses on best practices for containerization, security, and performance optimization.

## Key Capabilities

### Image Creation & Management
- Write optimized Dockerfiles with multi-stage builds
- Create custom base images and runtime images
- Implement layer caching and image size optimization
- Handle different architectures and platforms

### Container Orchestration
- Design docker-compose.yml files for multi-service applications
- Configure networking, volumes, and environment variables
- Implement health checks and restart policies
- Manage container dependencies and startup order

### Development Workflow
- Setup development environments with hot reloading
- Configure debugging and logging for containers
- Implement CI/CD pipelines with Docker
- Handle container security scanning and vulnerability management

### Troubleshooting & Optimization
- Debug container startup and runtime issues
- Analyze container performance and resource usage
- Fix networking and volume mounting problems
- Optimize image build times and container startup

### Production Deployment
- Implement production-ready container configurations
- Configure secrets management and environment isolation
- Setup monitoring and logging for containerized applications
- Handle container scaling and load balancing

## Usage Examples

### Multi-stage Dockerfile for Node.js app
```dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Production stage
FROM node:18-alpine AS production
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --chown=nextjs:nodejs ./public ./public
COPY --chown=nextjs:nodejs ./.next ./.next
USER nextjs
EXPOSE 3000
ENV PORT 3000
CMD ["npm", "start"]
```

### Docker Compose for full-stack application
```yaml
version: '3.8'
services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - REACT_APP_API_URL=http://backend:8080

  backend:
    build: ./backend
    ports:
      - "8080:8080"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/app

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=app
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

### Development environment with hot reload
```yaml
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - .:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
    command: npm run dev
```

## Common Patterns

### Multi-stage builds for smaller images
```dockerfile
FROM golang:1.21-alpine AS builder
WORKDIR /build
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o app .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /build/app .
CMD ["./app"]
```

### Environment-specific configurations
```yaml
version: '3.8'
services:
  web:
    image: myapp:${TAG:-latest}
    environment:
      - ENV=${ENV:-development}
    env_file:
      - .env.${ENV:-development}
    depends_on:
      - db
```

### Health checks and restart policies
```yaml
version: '3.8'
services:
  api:
    build: .
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
```

## Best Practices

### Image Optimization
- Use specific image tags instead of `latest`
- Minimize layer count and image size
- Leverage build cache effectively
- Remove unnecessary packages after installation

### Security
- Run containers as non-root user
- Use trusted base images
- Scan images for vulnerabilities
- Don't store secrets in images

### Networking & Volumes
- Use networks for service communication
- Implement proper volume mounting
- Configure resource limits
- Handle container logs appropriately

### Development Workflow
- Use .dockerignore files
- Implement multi-stage builds
- Setup development and production configurations
- Use environment variables for configuration

## Troubleshooting

### Container won't start
- Check logs: `docker logs <container>`
- Verify port conflicts and environment variables
- Ensure dependencies are running
- Check file permissions and user context

### Build failures
- Verify Dockerfile syntax and base images
- Check build context and .dockerignore
- Ensure required files are copied correctly
- Validate RUN commands and their outputs

### Performance issues
- Monitor resource usage with `docker stats`
- Check for memory leaks and CPU bottlenecks
- Optimize image layers and build cache
- Implement proper health checks

### Networking problems
- Verify network connectivity between containers
- Check port mappings and firewall rules
- Validate service discovery configuration
- Debug DNS resolution issues

## Integration Points

### Development Tools
- **VS Code**: Dev Containers, Docker extension
- **IntelliJ IDEA**: Docker plugin integration
- **GitHub Actions**: Container-based CI/CD workflows

### Orchestration Platforms
- **Docker Swarm**: Native clustering and orchestration
- **Kubernetes**: Container orchestration and management
- **Amazon ECS/EKS**: AWS container services
- **Google Cloud Run**: Serverless containers

### Cloud Platforms
- **AWS ECR**: Container registry and deployment
- **Google Container Registry**: GCR integration
- **Azure Container Registry**: ACR for Azure deployments
- **Docker Hub**: Public container registry

### CI/CD Tools
- **GitHub Actions**: Container-based workflows
- **GitLab CI**: Docker-in-Docker support
- **Jenkins**: Docker pipeline integration
- **CircleCI**: Containerized build environments

### Monitoring & Logging
- **Prometheus**: Container metrics collection
- **ELK Stack**: Centralized logging
- **Datadog**: Container monitoring and alerting
- **Grafana**: Visualization dashboards