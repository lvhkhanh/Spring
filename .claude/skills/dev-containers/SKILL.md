---
name: dev-containers
description: Assist with VS Code Dev Containers development, configuration, and management for consistent development environments.
INVOKES:
  - docker
  - bash
---

# Overview

The Dev Containers skill provides guidance for creating, configuring, and managing VS Code Dev Containers. It helps developers set up consistent, reproducible development environments using Docker containers, enabling seamless collaboration and eliminating "works on my machine" issues.

# Key Capabilities

- Create and configure devcontainer.json files for various project types
- Set up Docker-based development environments with custom tools and dependencies
- Configure VS Code extensions, settings, and workspace configurations
- Manage container lifecycle, networking, and volume mounting
- Implement multi-stage builds and optimized container images
- Handle environment variables, secrets, and configuration management
- Support for different container runtimes and orchestration platforms

# Usage Examples

1. Create a basic devcontainer.json for a Node.js project:

```json
{
  "name": "Node.js Dev Container",
  "image": "mcr.microsoft.com/devcontainers/javascript-node:18",
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {},
    "ghcr.io/devcontainers/features/docker-in-docker:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.vscode-typescript-next",
        "esbenp.prettier-vscode"
      ]
    }
  },
  "forwardPorts": [3000, 9229],
  "postCreateCommand": "npm install"
}
```

2. Set up a Python development environment:

```json
{
  "name": "Python Dev Container",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.black-formatter"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python"
      }
    }
  },
  "postCreateCommand": "pip install -r requirements.txt"
}
```

3. Configure a multi-service development environment:

```json
{
  "name": "Full Stack Dev Container",
  "dockerComposeFile": [
    "../docker-compose.yml",
    "docker-compose.dev.yml"
  ],
  "service": "app",
  "workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-vscode.vscode-json",
        "ms-vscode-remote.remote-containers"
      ]
    }
  }
}
```

# Common Patterns

- Use official Microsoft dev container images as base images for consistency
- Leverage dev container features to add common tools and runtimes
- Configure VS Code extensions and settings for team consistency
- Use docker-compose for multi-service applications
- Implement post-create commands for environment setup
- Mount volumes for persistent data and cache directories
- Configure port forwarding for web applications and debugging

# Best Practices

- Start with official base images and customize as needed
- Keep devcontainer.json files version-controlled with project code
- Use features instead of manual installations for common tools
- Configure appropriate VS Code extensions for the project type
- Set up proper port forwarding and networking
- Implement security best practices for container access
- Document custom configurations and setup requirements
- Test dev containers across different environments and platforms

# Troubleshooting

- Check that Docker is running and accessible from VS Code
- Verify that devcontainer.json syntax is valid JSON
- Ensure required ports are not already in use on the host
- Check container logs if build or startup fails
- Validate that all required features and extensions are available
- Test with different base images if compatibility issues occur
- Use VS Code's Dev Containers output panel for debugging
- Ensure proper file permissions and ownership in mounted volumes

# Integration Points

- VS Code: Primary IDE integration and extension management
- Docker: Container runtime and image management
- GitHub Codespaces: Cloud-based development environments
- GitHub Actions: CI/CD pipeline integration
- Docker Compose: Multi-service application orchestration
- Development tools: Language servers, linters, and formatters
- Cloud platforms: AWS, GCP, Azure container services
- Version control: Git integration and workspace management