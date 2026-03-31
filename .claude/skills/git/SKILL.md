---
name: git
description: '**WORKFLOW SKILL** — Manage Git repositories, branches, commits, merges, rebases, and workflows. USE FOR: creating commits; setting up branches; resolving merge conflicts; writing git hooks; releasing and tagging; reviewing history. DO NOT USE FOR: non-git version control systems; complex repo hosting administration; upstream CI/CD pipeline configuration. INVOKES: terminal commands for git operations, file system tools for repository modifications, semantic search for commit pattern discovery.'
---

# Git Repository Management

## Overview

This skill provides complete support for Git workflows, including repository initialization, branching strategies, commit and merge operations, conflict resolution, and release automation.

## Key Capabilities

### Repository Setup
- Initialize new Git repositories (`git init`)
- Clone remote repositories (`git clone`)
- Configure remotes (`git remote add`, `git remote set-url`)
- Manage .gitignore and git configuration files

### Branching & Workflow
- Create and switch branches (`git branch`, `git checkout`, `git switch`)
- Implement GitFlow, GitHub Flow, trunk-based workflows
- Cherry-pick commits (`git cherry-pick`)
- Backport fixes and manage release branches

### Commit Management
- Stage and unstage changes (`git add`, `git reset`)
- Create descriptive commits (`git commit`)
- Amend commits and rewrite history (`git commit --amend`)
- Squash commits (`git rebase -i`)

### Merging & Rebasing
- Merge feature branches (`git merge`)
- Rebase for linear history (`git rebase`)
- Resolve conflicts with proper markers
- Use `git mergetool` and conflict resolution strategies

### History & Inspection
- Show commit logs (`git log`, `git show`, `git diff`)
- Inspect branches and tags (`git branch -av`, `git tag`)
- View file history and annotations (`git blame`)

### Collaboration
- Push and pull changes (`git push`, `git pull`)
- Fetch updates (`git fetch`)
- Work with pull requests and reviews
- Set up and use signed commits (`git commit -S`)

## Usage Examples

### Initialize Repository
```
git init my-app
cd my-app
# create project files
git add .
git commit -m "Initial commit"
```

### Feature Branch Workflow
```
git checkout -b feature/add-login
# code changes
git add .
git commit -m "Add login feature"
git checkout main
git pull origin main
git merge feature/add-login
git push origin main
```

### Rebase and Squash
```
git checkout feature/cleanup
git fetch origin
git rebase origin/main
# resolve conflicts if any
git rebase --continue
git rebase -i HEAD~3
# squash commits as needed
git push --force-with-lease
```

## Common Patterns

### Code Review Preparation
- Rebase on latest main
- Squash cleanup commits
- Use `git diff` to inspect final changes
- Ensure tests pass locally

### Hotfix Flow
- `git checkout -b hotfix/issue-123 origin/main`
- Apply fix, commit, and push
- Merge into `main` and `develop` if using GitFlow

### Conflict Resolution
- Use `git status` to identify conflicted files
- Edit files to resolve markers (`<<<<<<<`, `=======`, `>>>>>>>`)
- `git add` resolved files
- `git rebase --continue` or `git merge --continue`

## Best Practices

- Write clear commit messages with intent and scope
- Keep branches small and focused
- Rebase feature branches before final merge
- Avoid force pushing to shared branches unless necessary
- Use tags (`git tag`) for release milestones
- Configure `.gitattributes` for line endings and merge strategies
- Use `git hooks` for linting and pre-commit checks

## Troubleshooting

### Common Issues
- **Detached HEAD**: use `git checkout <branch>` or create a new branch
- **Merge conflicts**: resolve with markers and commit
- **Untracked files**: add to .gitignore or stage files
- **Local/remote divergence**: use `git pull --rebase` or `git push --force-with-lease` carefully

### Validation Steps
1. `git status` for workspace state
2. `git log --oneline --graph --all` for commit structure
3. `git diff --cached` to inspect staged changes
4. `git fsck` for repository integrity

## Integration Points

- CI/CD: GitHub Actions, GitLab CI, Jenkins
- Code review: GitHub PRs, GitLab MRs, Bitbucket
- Repo hosts: GitHub, GitLab, Azure DevOps
- Automation: hooks (`pre-commit`, `post-commit`), scripts
- Release: semantic versioning, changelog generation
