---
name: macos
description: '**WORKFLOW SKILL** — Create, configure, and troubleshoot macOS workflows, scripts, and environment setup. USE FOR: macOS automation, shell scripts with zsh/bash, Homebrew package management, system settings, file permissions, and developer tooling. DO NOT USE FOR: non-macOS platforms, hardware repair, or unrelated OS-specific administration. INVOKES: terminal commands, file system operations, and configuration file editing.'
---

# macOS Skill

## Overview

This skill provides macOS-specific guidance for developers and operators. It includes command-line workflows, environment setup, automation, system diagnostics, and best practices for security and productivity on macOS.

## Key Capabilities

### Setup & Initialization
- Install and configure Homebrew, Xcode Command Line Tools, and Rosetta 2
- Setup shell environments (zsh, bash) with prompt, aliases, and scripts
- Configure SSH keys, Git, .gitconfig, and macOS keychain integration
- Manage user profiles, directories, permissions, and environment variables

### Package & App Management
- Install/uninstall packages with `brew`, `brew cask`, and `mas`
- Upgrade packages, cleanup old versions, and resolve formula conflicts
- Automate app installs for dev, office, and productivity workflows
- Manage launch agents and daemons with `launchctl`

### File & System Operations
- Work with macOS file system, Finder defaults, path handling, hard/soft links
- Set file permissions, ACLs, and secure directory access with `chmod`/`chown`
- Use `mdfind`, `mdls`, `mdutil`, and `find` for advanced file searches
- Manage disk usage with `df`, `du`, and `diskutil`

### Networking and Security
- Configure Wi-Fi, VPN, firewall settings, and network diagnostics (`ifconfig`, `ping`, `route`)
- Manage certificates in Keychain Access with `security` CLI
- Apply security settings via `sudo defaults write` for privacy and hardening
- Troubleshoot network performance and DNS resolution issues

### Development Tooling
- Setup IDEs: VS Code, IntelliJ, Xcode, and their CLI helpers
- Configure language runtimes: Python (pyenv), Node.js (nvm), Java (SDKMAN™), Ruby (rbenv)
- Create automation with AppleScript, `osascript`, and Automator workflows
- Use `tmutil` for Time Machine backups and restore operations

## Usage Examples

### Install Homebrew and core tools
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git python node
```

### Configure zsh environment
```
cat <<'EOF' >> ~/.zshrc
export PATH="/usr/local/bin:$PATH"
alias ll='ls -lah'
EOF
source ~/.zshrc
```

### Mount and unmount a disk image
```
hdiutil attach /path/to/image.dmg
hdiutil detach /Volumes/VolumeName
```

### Add macOS defaults for Finder and Dock
```
defaults write com.apple.finder AppleShowAllFiles -bool true
killall Finder
```

## Common Patterns

### Homebrew Bundle for reproducible setup
```
tap 'Homebrew/bundle'
brew bundle dump --file=~/Brewfile
brew bundle --file=~/Brewfile
```

### Automated backup using Time Machine
```
sudo tmutil setdestination /Volumes/Backup
sudo tmutil startbackup --auto
```

### Resolve permission issues
```
sudo chown -R $(whoami):staff ~/Projects
chmod -R u+rwX ~/Projects
```

### Use `launchctl` to load a user agent
```
launchctl unload ~/Library/LaunchAgents/com.example.agent.plist
launchctl load ~/Library/LaunchAgents/com.example.agent.plist
```

## Best Practices

- Keep macOS and installed software up to date
- Backup with Time Machine and verify via `tmutil verifychecksums`
- Use `brew bundle` for environment reproducibility and share Brewfile
- Keep shell config small, modular, and source external dotfiles
- Prefer secure defaults for keychain and firewall policy
- Use `brew doctor` and `brew update` routinely

## Troubleshooting

### Homebrew issues
- `brew doctor` for diagnostics
- Remove stale symlinks with `brew cleanup`
- Reinstall a broken formula: `brew reinstall <formula>`

### Xcode command line tools
- Install with `xcode-select --install`
- Switch paths: `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`

### Network issues
- Flush DNS cache: `sudo dscacheutil -flushcache && sudo killall -HUP mDNSResponder`
- Reset network interfaces with `networksetup -setairportpower en0 off` and on

### Performance and disk
- Find big files: `sudo du -hxd 1 / | sort -h | tail -n 20`
- Reset spotlight indexing: `sudo mdutil -E /`

## Integration Points

- Homebrew (package manager) and Brewfile automation
- AppleScript / Automator workflows for UI automation
- Auth and security with Keychain Access CLI
- Developer environments: xcode-select, pyenv, nvm, sdkman, rbenv
- macOS system settings via `defaults` and `sudo` configuration CLI
