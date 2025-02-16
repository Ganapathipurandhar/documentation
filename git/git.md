# **Git Cheat Sheet**

## **Initializing a Repository**  
```bash
git init  # Initialize a new Git repository
```
### Configuring Git
```sh
# Set user name
git config --global user.name "Your Name"

# Set user email
git config --global user.email "your.email@example.com"

## **Staging and Committing**  
```bash
git add .           # Stage all changes  
git add <file>      # Stage a specific file  
git commit -m "message"  # Commit staged changes with a message  
```

## **Checking Changes**  
```bash
git diff --cached   # Show changes in the staging area  
git restore --staged <file>  # Unstage a file  
```

## **Viewing Commit History**  
```bash
git log --name-only        # Show commit history with file names  
git log -n 1               # Show the latest commit  
git log -1 --oneline       # Show the latest commit in a single line  
git log -1 --pretty=format:"%h - %an - %s" -- *.js  # Show details of the last commit for JS files  
git log -p -1 <commit-hash>  # Show the changes of a specific commit  
git show <commit-hash>      # Show details of a specific commit  
```

## **Removing Files**  
```bash
git rm <file> --cached  # Remove a file from staging (keep in working directory)  
git rm -f <file>        # Forcefully remove a file  
```

## **Fetching and Merging**  
```bash
git fetch           # Fetch changes from the remote repository  
git merge           # Merge fetched changes  
git pull            # Fetch and merge changes (same as above combined)  
```

## **Pull Requests (PR)**  
1. Raise a pull request (PR).  
2. Reviewers (on the right side of the PR) , reviewer names the will be they.  
3. Changes must be approved under the **"Files Changed"** tab.  
4. Once approved, merge the changes into `main` or `master`.  

## **Handling Merge Conflicts**  
- If multiple people work on the same repo, merge conflicts may occur.  
- Manually adjust the conflicting code, stage the changes, and push again.  

## **Forking a Repository**  
- If you don’t have write access, **fork** the repository.  
- Clone the forked repo, make changes, and raise a PR.  
- If approved, the changes will be merged into the main repository.  

## **Rebasing and Cherry-Picking**  
```bash
git rebase -i HEAD~n  # Squash multiple commits into one  
git cherry-pick <commit-hash>  # Apply a specific commit from another branch  
```

## **Undoing Changes**  
```bash
git revert <commit-hash>  # Revert a commit (creates a new commit)  
git reset --soft HEAD~1  # Undo the last commit (keep changes staged)  
git reset --hard HEAD~1  # Undo the last commit (discard changes)  
git reflog  # Recover changes after a hard reset  
```

## **Stashing Changes**  
```bash
git stash          # Save uncommitted changes temporarily  
git stash list     # Show stashed changes  
git stash show <stash@{n}>  # Show details of a specific stash  
git stash pop      # Apply and remove the most recent stash  
```

## **Resetting to a Specific Commit**  
```bash
git reset --hard <commit-hash>  # Reset to a specific commit  
```

## **Working with SSH Keys**  
```bash
ssh-keygen.exe  # Generate an SSH key  
```

## **Cloning a Repository**  
```bash
git clone <repo-url>  # Clone a repository  
##  Branching Strategies

### Git Flow
- **Main Branch (main/master):** Stable production-ready code.
- **Develop Branch (develop):** Integration branch for features.
- **Feature Branches (feature/xyz):** Branch for new features.
- **Release Branches (release/x.y.z):** Prepares for production release.
- **Hotfix Branches (hotfix/x.y.z):** Fixes critical issues in production.

### GitHub Flow
- **Main branch:** Always deployable.
- **Feature branches:** Created from main, merged after PR review.
- **Pull Requests:** Required before merging.

### Trunk-Based Development
- **Main branch is always deployable.**
- **Short-lived feature branches.**
- **Continuous integration.**

## 3. Working with Branches
```sh
# Create a new branch
git checkout -b feature-branch

# Switch to another branch
git checkout develop

# Merge a branch into the current branch
git merge feature-branch

# Delete a branch
git branch -d feature-branch
```

## 4. Creating a Pull Request (PR)
1. Push changes to a feature branch:
   ```sh
   git checkout -b feature-branch
   git add .
   git commit -m "Implemented feature XYZ"
   git push origin feature-branch
   ```
2. Go to GitHub/GitLab/Bitbucket.
3. Navigate to the repository and open a **Pull Request**.
4. Select **base branch** and **compare branch**.
5. Add a description and request reviews.
6. Merge once approved.

## 5. Python Script to Get Last 30 Commits by Developers
```python
import subprocess

def get_last_30_commits():
    command = "git log --pretty=format:'%h - %an - %s' -n 30"
    commits = subprocess.check_output(command, shell=True, text=True)
    print("Last 30 commits:")
    print(commits)

if __name__ == "__main__":
    get_last_30_commits()
```

## 6. Undoing Changes
```sh
# Undo the last commit (soft reset, keeps changes in working directory)
git reset --soft HEAD~1

# Undo the last commit (hard reset, discards changes)
git reset --hard HEAD~1

# Remove a file from staging area
git reset HEAD <file>
```

## 7. Managing Remote Repositories
```sh
# Add a remote repository
git remote add origin <repository-url>

# View remote repositories
git remote -v

# Push changes to remote
git push origin main

# Fetch and merge changes from remote
git pull origin main
```

## 8. Best Practices for Git in DevOps
- **Use meaningful commit messages.**
- **Follow a consistent branching strategy.**
- **Use PR reviews and automated tests before merging.**
- **Rebase instead of merging when appropriate.**
- **Keep repositories clean and avoid large binary files.**
- **Enforce access controls and branch protections.**
- **Automate workflows with GitHub Actions or GitLab CI/CD.**