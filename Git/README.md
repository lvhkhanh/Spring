# Git
## Branches
### main(master)
`git init`
### develop
`git checkout -b develop`
### feature
`git checkout develop
git merge feature/<f1>`
`git flow feature finish feature/<f1>`
### release
```
git checkout develop
git checkout -b release/v0.0.1
```
`git flow release start v0.0.1`
`git checkout main
git merge release/v0.0.1`
`git flow release finish v0.0.1`
### hotfix
```
git checkout main
git checkout -b hotfix/hf1
```
`git flow hotfix start hotfix/hf1`
```
git checkout main
git merge hotfix/hf1
git checkout develop
git merge hotfix/hf1
git branch -D hotfix/hf1
```
`git flow hotfix finish hotfix/hf1`