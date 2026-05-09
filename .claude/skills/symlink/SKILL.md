---
name: symlink
description: '**WORKFLOW SKILL** — Create, manage, inspect, and troubleshoot symbolic links and hard links across Linux, macOS, and Windows. USE FOR: symlink creation and removal, hard link management, relative vs absolute link strategies, cross-platform linking differences, link resolution and debugging, dotfile and config symlinking, monorepo and workspace linking, deployment symlink patterns, and link-related permission issues. DO NOT USE FOR: network shares or mounted drives (use mount/NFS skills), URL redirects, or application-level aliasing. INVOKES: terminal for link commands, file system tools for inspection and verification.'
---

# Symbolic Link Skill

## Overview

This skill provides comprehensive support for creating, managing, inspecting, and troubleshooting symbolic links (symlinks) and hard links across Linux, macOS, and Windows. It covers everyday linking tasks, dotfile management, monorepo workspace linking, deployment patterns, and cross-platform considerations.

## Key Capabilities

### Symlink Creation and Management

- Create symbolic links to files and directories
- Create hard links to files
- Remove, replace, and update existing links
- Use relative vs absolute paths strategically
- Batch-create links from configuration or scripts
- Verify link targets and resolve chains

### Cross-Platform Linking

- Linux and macOS: `ln -s` for symlinks, `ln` for hard links
- Windows: `mklink`, `New-Item -ItemType SymbolicLink`, junction points
- Handle platform-specific permission requirements (Windows Developer Mode, elevated privileges)
- Git symlink handling across platforms (`core.symlinks` config)

### Dotfile and Configuration Management

- Symlink dotfiles from a central repository to home directory
- Manage tool configs (`.bashrc`, `.zshrc`, `.gitconfig`, `.vimrc`, etc.) via symlinks
- Use stow, chezmoi, or manual scripts for dotfile orchestration
- Handle XDG base directory symlink patterns

### Monorepo and Workspace Linking

- Link shared packages in monorepo setups (npm/yarn/pnpm workspaces)
- Use `npm link` / `yarn link` / `pnpm link` for local package development
- Symlink shared configuration files across packages
- Handle `node_modules` symlink resolution

### Deployment and Operations

- Blue-green deployment symlink swaps (`current` → `release-v2`)
- Log directory and shared asset linking
- Mount point and data directory symlinking
- Rollback via symlink repointing

## Usage Examples

### Create a Symlink

```
Create a symbolic link from ~/dotfiles/.zshrc to ~/.zshrc
so my shell config is version-controlled.
```

### Debug a Broken Symlink

```
Find and fix all broken symlinks in /var/www/app
after a deployment.
```

### Set Up Dotfile Symlinks

```
Write a script that symlinks all config files
from my ~/dotfiles repo to their correct locations.
```

### Blue-Green Deployment Swap

```
Set up symlink-based blue-green deployment
where /var/www/current points to the active release directory.
```

### Cross-Platform Symlink in Git

```
Configure a Git repository to handle symlinks correctly
on both macOS and Windows.
```

## Common Patterns

### Basic Symlink Operations (Linux / macOS)

```bash
# Create a symbolic link (symlink)
ln -s /path/to/target /path/to/link

# Create a symbolic link to a directory
ln -s /path/to/target-dir /path/to/link-dir

# Create a hard link (files only, same filesystem)
ln /path/to/target /path/to/hardlink

# Create a relative symlink
ln -s ../shared/config.yml ./config.yml

# Force-replace an existing symlink
ln -sf /path/to/new-target /path/to/existing-link

# Create symlink with no-dereference (replace symlink to directory)
ln -sfn /path/to/new-target-dir /path/to/existing-link-dir

# Remove a symlink (does NOT delete the target)
rm /path/to/link
# or
unlink /path/to/link
```

### Inspect and Resolve Symlinks

```bash
# Check if a path is a symlink
test -L /path/to/link && echo "Is a symlink" || echo "Not a symlink"

# Read the target of a symlink
readlink /path/to/link

# Resolve the full canonical path (follows all symlinks)
readlink -f /path/to/link          # Linux
readlink /path/to/link             # macOS (single level)
realpath /path/to/link             # Linux and macOS (with coreutils)

# Show symlink details with ls
ls -la /path/to/link

# Find all symlinks in a directory
find /path/to/dir -type l

# Find all broken symlinks
find /path/to/dir -type l ! -exec test -e {} \; -print

# Find all symlinks pointing to a specific target
find /path/to/dir -type l -lname '*/target-name'
```

### Windows Symlink Operations

```powershell
# Create a file symlink (requires Developer Mode or admin)
New-Item -ItemType SymbolicLink -Path "C:\link.txt" -Target "C:\target.txt"

# Create a directory symlink
New-Item -ItemType SymbolicLink -Path "C:\link-dir" -Target "C:\target-dir"

# Create a junction point (directory only, no admin required)
New-Item -ItemType Junction -Path "C:\junction-dir" -Target "C:\target-dir"

# Create a hard link
New-Item -ItemType HardLink -Path "C:\hardlink.txt" -Target "C:\target.txt"

# Using mklink (CMD)
mklink "C:\link.txt" "C:\target.txt"           # File symlink
mklink /D "C:\link-dir" "C:\target-dir"        # Directory symlink
mklink /J "C:\junction" "C:\target-dir"        # Junction point
mklink /H "C:\hardlink.txt" "C:\target.txt"    # Hard link

# Check if path is a symlink
(Get-Item "C:\link.txt").Attributes -match 'ReparsePoint'

# Read symlink target
(Get-Item "C:\link.txt").Target

# Remove a symlink
Remove-Item "C:\link.txt"
(Remove-Item "C:\link-dir" -Force)  # For directory symlinks
```

### Dotfile Management Script

```bash
#!/usr/bin/env bash
# dotfiles/install.sh — Symlink dotfiles to home directory

set -euo pipefail

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"

# Map: source (relative to DOTFILES_DIR) → target
declare -A LINKS=(
  [".zshrc"]="$HOME/.zshrc"
  [".gitconfig"]="$HOME/.gitconfig"
  [".vimrc"]="$HOME/.vimrc"
  [".tmux.conf"]="$HOME/.tmux.conf"
  ["config/starship.toml"]="$HOME/.config/starship.toml"
  ["config/alacritty/alacritty.toml"]="$HOME/.config/alacritty/alacritty.toml"
)

for src in "${!LINKS[@]}"; do
  source_path="$DOTFILES_DIR/$src"
  target_path="${LINKS[$src]}"

  # Create parent directory if needed
  mkdir -p "$(dirname "$target_path")"

  # Back up existing file if it's not already a symlink
  if [[ -e "$target_path" && ! -L "$target_path" ]]; then
    echo "Backing up existing $target_path → ${target_path}.bak"
    mv "$target_path" "${target_path}.bak"
  fi

  # Create or replace symlink
  ln -sf "$source_path" "$target_path"
  echo "Linked $source_path → $target_path"
done

echo "Dotfiles installed."
```

### GNU Stow for Dotfiles

```bash
# Directory structure for stow:
# ~/dotfiles/
#   zsh/
#     .zshrc
#   git/
#     .gitconfig
#   vim/
#     .vimrc

# Symlink all zsh dotfiles to $HOME
cd ~/dotfiles
stow zsh        # Creates ~/.zshrc → dotfiles/zsh/.zshrc

# Symlink multiple packages
stow zsh git vim

# Remove symlinks for a package
stow -D zsh

# Re-stow (remove then re-link, useful after changes)
stow -R zsh

# Preview what stow would do (dry run)
stow -n -v zsh

# Use a custom target directory
stow -t /etc nginx
```

### Blue-Green Deployment Pattern

```bash
#!/usr/bin/env bash
# deploy.sh — Symlink-based blue-green deployment

set -euo pipefail

APP_DIR="/var/www/app"
RELEASES_DIR="$APP_DIR/releases"
CURRENT_LINK="$APP_DIR/current"
SHARED_DIR="$APP_DIR/shared"

RELEASE_NAME="$(date +%Y%m%d%H%M%S)"
RELEASE_DIR="$RELEASES_DIR/$RELEASE_NAME"

echo "Deploying release $RELEASE_NAME..."

# 1. Create release directory and extract/copy app files
mkdir -p "$RELEASE_DIR"
tar -xzf /tmp/app-build.tar.gz -C "$RELEASE_DIR"

# 2. Symlink shared resources into the release
ln -sf "$SHARED_DIR/logs" "$RELEASE_DIR/logs"
ln -sf "$SHARED_DIR/.env" "$RELEASE_DIR/.env"
ln -sf "$SHARED_DIR/uploads" "$RELEASE_DIR/public/uploads"

# 3. Atomically swap the current symlink
# ln -sfn is atomic on most filesystems
ln -sfn "$RELEASE_DIR" "$CURRENT_LINK"

echo "Release $RELEASE_NAME is now live at $CURRENT_LINK"

# 4. Clean up old releases (keep last 5)
cd "$RELEASES_DIR"
ls -1dt */ | tail -n +6 | xargs rm -rf --
echo "Old releases cleaned up."
```

### Rollback via Symlink

```bash
#!/usr/bin/env bash
# rollback.sh — Revert to the previous release

APP_DIR="/var/www/app"
RELEASES_DIR="$APP_DIR/releases"
CURRENT_LINK="$APP_DIR/current"

# Get the currently active release
CURRENT_RELEASE="$(readlink -f "$CURRENT_LINK")"
CURRENT_NAME="$(basename "$CURRENT_RELEASE")"

# Find the previous release
PREVIOUS_RELEASE="$(ls -1dt "$RELEASES_DIR"/*/ | grep -v "$CURRENT_NAME" | head -1)"

if [[ -z "$PREVIOUS_RELEASE" ]]; then
  echo "No previous release found to roll back to."
  exit 1
fi

echo "Rolling back from $CURRENT_NAME to $(basename "$PREVIOUS_RELEASE")..."
ln -sfn "$PREVIOUS_RELEASE" "$CURRENT_LINK"
echo "Rollback complete. Active: $(readlink -f "$CURRENT_LINK")"
```

### npm / yarn / pnpm Link for Local Development

```bash
# npm link — register a local package globally, then link into consumer
cd ~/projects/my-library
npm link                          # Registers globally

cd ~/projects/my-app
npm link my-library               # Creates symlink in node_modules

# Unlink when done
cd ~/projects/my-app
npm unlink my-library

cd ~/projects/my-library
npm unlink

# yarn link
cd ~/projects/my-library
yarn link

cd ~/projects/my-app
yarn link my-library

# pnpm link
cd ~/projects/my-app
pnpm link ~/projects/my-library   # Direct path, no global step
```

### Git Symlink Configuration

```bash
# Enable symlink support (important on Windows)
git config --global core.symlinks true

# Check current symlink setting
git config --get core.symlinks

# Add a symlink to a Git repository
ln -s ../shared/config.yml config.yml
git add config.yml
git commit -m "Add symlink to shared config"

# .gitattributes — force symlink handling
# (useful when some clones may not support symlinks)
config.yml symlink=true
```

## Best Practices

### Relative vs Absolute Paths

- Use **relative** symlinks when both link and target live in the same project or repository — they survive directory moves and are portable across machines
- Use **absolute** symlinks when linking to system paths, shared directories, or locations outside the project tree
- Use `ln -sr` (GNU coreutils) to auto-compute relative paths: `ln -sr /a/b/target /a/c/link`
- In deployment scripts, always resolve the target to a canonical path before linking

### Safety and Idempotency

- Always check if a link already exists before creating: `[[ -L "$link" ]]`
- Use `ln -sf` to force-replace file symlinks; use `ln -sfn` for directory symlinks
- Back up non-symlink files before replacing them with links
- Use `unlink` or `rm` to remove symlinks — never use `rm -r` on a symlink to a directory (it may delete contents on some systems)
- Make install/link scripts idempotent — safe to run multiple times

### Symlink Chains

- Avoid deep symlink chains (A → B → C → D) as they make debugging difficult
- Most systems limit symlink resolution depth (typically 40 levels)
- Use `readlink -f` or `realpath` to resolve the final target for diagnostics
- Document intentional symlink chains in README or deploy scripts

### Permissions and Ownership

- Symlinks inherit the permissions of their target, not their own metadata
- `chmod` on a symlink changes the target's permissions (on most systems)
- `chown -h` changes the symlink owner itself (not the target)
- On Windows, creating symlinks requires Developer Mode or Administrator privileges
- On SELinux systems, symlink targets may need correct security contexts

### Version Control

- Git stores symlinks as text files containing the target path
- On Windows clones without symlink support, Git creates plain text files instead
- Use `.gitattributes` or document the requirement for `core.symlinks = true`
- Avoid committing absolute symlinks — they break on other machines
- Consider using build scripts to create platform-specific links at setup time

### Cross-Platform Considerations

- macOS and Linux: `ln -s` works identically for most use cases
- Windows: prefer `New-Item -ItemType SymbolicLink` in PowerShell; use junction points for directories when admin rights are unavailable
- Docker: symlinks in bind mounts may not resolve if targets are outside the mounted path
- Network filesystems (NFS, SMB): symlink behavior varies — test before relying on them

## Troubleshooting

### Broken Symlinks

- **Symptom**: `ls` shows the link in red; file operations fail with "No such file or directory"
- **Cause**: target was moved, renamed, or deleted
- **Fix**: update or recreate the symlink to the correct target
- **Find all broken links**: `find /path -type l ! -exec test -e {} \; -print`

### Permission Denied Creating Symlinks

- **Linux/macOS**: check write permission on the directory where the link is created (not the target)
- **Windows**: enable Developer Mode (`Settings → Update & Security → For developers`) or run as Administrator
- **Docker**: ensure the user inside the container has write access to the mount point

### Symlink Not Followed

- **`cp`, `rsync`**: by default copy the link, not the target — use `cp -L` or `rsync -L` to follow
- **`tar`**: use `tar -h` to dereference symlinks when archiving
- **Web servers**: Nginx and Apache may need explicit config to follow symlinks (`Options FollowSymLinks` in Apache, `disable_symlinks off` in Nginx)
- **Docker COPY**: `COPY` in Dockerfile does not follow symlinks outside build context

### Circular Symlinks

- **Symptom**: "Too many levels of symbolic links" error
- **Cause**: A → B → A or longer cycles
- **Fix**: use `readlink` on each link in the chain to find the loop, then break it by removing or repointing one link

### Git Symlinks on Windows

- **Symptom**: symlinks appear as plain text files containing the target path
- **Cause**: `core.symlinks` is false or Developer Mode is off
- **Fix**: enable Developer Mode, set `git config --global core.symlinks true`, and re-clone

### node_modules Symlink Issues

- **Symptom**: module not found errors after `npm link` or in monorepo workspaces
- **Cause**: Node.js resolves the real path of symlinks, which changes `__dirname` and module resolution
- **Fix**: use `--preserve-symlinks` flag, or configure bundler `resolve.symlinks` setting (Webpack: `resolve.symlinks: false`)

## Integration Points

- **Shell**: bash, zsh, fish, PowerShell — all support symlink creation and inspection
- **Dotfile managers**: GNU Stow, chezmoi, yadm, rcm, dotbot
- **Package managers**: npm link, yarn link, pnpm link, pip install -e, go mod replace
- **Deployment**: Capistrano, Deployer, custom blue-green scripts
- **Containers**: Docker bind mounts, volume symlinks, build context linking
- **Web servers**: Nginx, Apache, Caddy — symlink following configuration
- **Version control**: Git `core.symlinks`, `.gitattributes`, pre-checkout hooks
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins — symlink creation in build steps
- **Build tools**: Webpack, Vite, esbuild — `resolve.symlinks` configuration
