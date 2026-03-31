---
name: vscode-extensions
description: "**WORKFLOW SKILL** — Install, manage, and configure VS Code extensions programmatically. USE FOR: installing extensions via command line, managing extension dependencies, automating workspace setup, checking installed extensions, uninstalling extensions. DO NOT USE FOR: general coding questions; runtime debugging or error diagnosis; VS Code extension development. INVOKES: terminal commands for extension management, file system tools for configuration files."
---

# VS Code Extensions Management Skill

## Overview

This skill provides comprehensive capabilities for managing VS Code extensions through command-line operations. It enables automated installation, verification, and removal of extensions, making it ideal for setting up development environments, managing team extension requirements, and maintaining consistent tooling across projects.

## Key Capabilities

### Extensions
- [ ] Claude Code for VS Code

### Extension Installation
- **Single Extension Installation**: Install individual extensions using publisher.extension format
- **Bulk Installation**: Install multiple extensions in batch operations
- **Installation Verification**: Confirm successful installation with return status checking

### Extension Management
- **List Installed Extensions**: Retrieve complete list of currently installed extensions
- **Extension Removal**: Uninstall extensions that are no longer needed
- **Status Checking**: Verify extension installation status and handle errors gracefully

### Error Handling
- **Robust Error Management**: Comprehensive exception handling for installation failures
- **Detailed Logging**: Clear error messages for troubleshooting installation issues
- **Graceful Degradation**: Continue operations even when individual extensions fail

## Usage Examples

### Installing Essential Development Extensions

```python
installer = VSCodeExtensionInstaller()

# Install core development extensions
essential_extensions = [
    "ms-python.python",
    "ms-vscode.vscode-typescript-next",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-json",
    "redhat.vscode-yaml"
]

results = installer.install_extensions(essential_extensions)
print(f"Installation results: {results}")
```

### Setting Up Data Science Environment

```python
# Install data science and notebook extensions
data_science_extensions = [
    "ms-toolsai.jupyter",
    "ms-python.python",
    "ms-toolsai.vscode-jupyter-powertoys",
    "ms-vscode.vscode-json",
    "redhat.vscode-yaml"
]

installer = VSCodeExtensionInstaller()
installer.install_extensions(data_science_extensions)
```

### Checking and Cleaning Extensions

```python
installer = VSCodeExtensionInstaller()

# List all installed extensions
installed = installer.get_installed_extensions()
print(f"Total extensions installed: {len(installed)}")

# Remove unwanted extensions
unwanted = ["some.unwanted-extension", "old.deprecated-extension"]
for ext in unwanted:
    if ext in installed:
        installer.uninstall_extension(ext)
```

## Best Practices

### Extension Selection
- **Verify Extension IDs**: Always use correct publisher.extension format
- **Check Compatibility**: Ensure extensions are compatible with your VS Code version
- **Review Permissions**: Be aware of extension permissions and data access

### Installation Strategy
- **Batch Operations**: Use bulk installation for multiple extensions to improve efficiency
- **Error Handling**: Always check installation results and handle failures appropriately
- **Dependency Management**: Install required extensions before dependent ones

### Maintenance
- **Regular Audits**: Periodically review installed extensions for relevance
- **Version Updates**: Keep extensions updated for security and feature improvements
- **Workspace Consistency**: Use consistent extension sets across team environments

## Troubleshooting

### Common Installation Issues

**Extension Not Found**
```
Error: Extension 'invalid.publisher' not found
```
- Verify the extension ID format (publisher.extension)
- Check if the extension exists in VS Code Marketplace
- Ensure correct spelling and case sensitivity

**Permission Denied**
```
Error: EACCES: permission denied
```
- Run VS Code with appropriate permissions
- Use sudo/admin privileges if necessary
- Check file system permissions for extension directory

**Network Issues**
```
Error: ECONNREFUSED or timeout errors
```
- Verify internet connectivity
- Check proxy settings if applicable
- Retry installation after network issues are resolved

### Verification Steps

1. **Check VS Code Installation**
   ```bash
   code --version
   ```

2. **Verify Extension Directory**
   ```bash
   ls ~/.vscode/extensions/
   ```

3. **Test Extension Installation**
   ```python
   installer = VSCodeExtensionInstaller()
   success = installer.install_extension("ms-vscode.vscode-json")
   print(f"Test installation: {'Success' if success else 'Failed'}")
   ```

## Integration Points

### Development Workflows
- **CI/CD Pipelines**: Automate extension installation in containerized environments
- **Team Onboarding**: Standardize development environments across team members
- **Project Setup**: Include extension requirements in project documentation

### IDE Management
- **Workspace Configuration**: Manage extensions per workspace or globally
- **Settings Synchronization**: Coordinate with VS Code settings sync features
- **Extension Packs**: Work with curated extension collections

### System Administration
- **Automated Provisioning**: Set up development machines programmatically
- **Environment Standardization**: Ensure consistent tooling across different systems
- **Dependency Tracking**: Maintain records of required extensions for projects