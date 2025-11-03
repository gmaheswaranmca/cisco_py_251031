## Git Basics

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. It allows multiple developers to work on the same codebase simultaneously, tracking changes and enabling collaboration.

### Key Concepts

- **Repository (Repo):** A directory containing your project files and a `.git` folder, which stores all version history and configuration.
- **Commit:** A snapshot of your files at a specific point in time. Each commit has a unique ID (SHA hash) and a message describing the change.
- **Working Directory:** The folder where you edit files. Changes here are not tracked until staged and committed.
- **Staging Area (Index):** A place to group changes before committing them. You add files to the staging area using `git add`.
- **HEAD:** A pointer to the latest commit in the current branch.

### Common Git Commands

- `git init`: Initializes a new Git repository in the current directory.
- `git clone <url>`: Creates a local copy of a remote repository.
- `git status`: Shows the status of changes as untracked, modified, or staged.
- `git add <file>`: Stages changes for the next commit.
- `git commit -m "message"`: Commits staged changes with a descriptive message.
- `git log`: Displays the commit history.

### Workflow Overview

1. **Initialize or Clone:** Start by creating a new repo (`git init`) or cloning an existing one (`git clone`).
2. **Edit Files:** Make changes in your working directory.
3. **Stage Changes:** Use `git add` to move changes to the staging area.
4. **Commit:** Save changes to the repository with `git commit`.
5. **Review History:** Use `git log` to view previous commits.

### Benefits of Using Git

- Tracks changes and history.
- Facilitates collaboration.
- Enables branching and merging.
- Supports distributed workflows.


```
```


## Branching & Merging

Branching and merging are core features of Git that enable parallel development and collaboration.

### Branching

A branch in Git is a lightweight movable pointer to a commit. Branches allow you to work on new features, bug fixes, or experiments in isolation from the main codebase.

- **Default Branch:** Most repositories have a default branch called `main` or `master`.
- **Creating a Branch:** Use `git branch <branch-name>` to create a new branch.
- **Switching Branches:** Use `git checkout <branch-name>` or `git switch <branch-name>` to move between branches.
- **Listing Branches:** Use `git branch` to see all local branches.

#### Example Workflow

```bash
git branch feature/login      # Create a new branch
git switch feature/login     # Switch to the new branch
# Make changes and commit
git add .
git commit -m "Add login feature"
```

### Merging

Merging combines changes from one branch into another, typically integrating a feature branch into the main branch.

- **Fast-forward Merge:** If the main branch has not changed since the feature branch was created, Git simply moves the pointer forward.
- **Three-way Merge:** If both branches have new commits, Git creates a new merge commit that combines changes.

#### Merge Commands

- `git merge <branch-name>`: Merge the specified branch into the current branch.
- `git merge --no-ff <branch-name>`: Forces a merge commit even if a fast-forward is possible.

#### Resolving Merge Conflicts

Conflicts occur when changes in two branches overlap. Git marks the conflicting files, and you must manually resolve them before completing the merge.

```bash
# After a conflict
# Edit files to resolve conflicts
git add <resolved-file>
git commit
```

### Best Practices

- Keep branches focused and short-lived.
- Regularly pull changes from the main branch to minimize conflicts.
- Delete branches after merging to keep the repository clean.

### Benefits

- Enables parallel development.
- Isolates features and fixes.
- Simplifies collaboration and code review.
- Makes it easy to experiment without affecting the main codebase.


```
```

## Synchronize

Synchronization in Git refers to keeping your local repository up-to-date with a remote repository and sharing your changes with others. This is essential for collaboration and ensuring everyone works with the latest code.

### Remote Repositories

A remote repository is a version of your project hosted on a server (e.g., GitHub, GitLab). You can connect your local repository to one or more remotes.

- **Adding a Remote:** Use `git remote add <name> <url>` to link a remote repository.
- **Viewing Remotes:** Use `git remote -v` to list configured remotes.

### Fetching and Pulling

- **git fetch:** Downloads new data from the remote repository but does not update your working files. It updates your local copy of the remote branches.
- **git pull:** Combines `git fetch` and `git merge`. It downloads changes and merges them into your current branch.

```bash
git fetch origin           # Fetch changes from 'origin' remote
git pull origin main       # Fetch and merge changes from 'main' branch
```

### Pushing Changes

After committing changes locally, you can share them with others by pushing to the remote repository.

- **git push:** Uploads your commits to the remote branch.

```bash
git push origin main       # Push local 'main' branch to remote 'origin'
```

### Handling Upstream Changes

If others have pushed changes to the remote repository, you should pull those changes before pushing your own to avoid conflicts.

- **git pull --rebase:** Re-applies your local commits on top of the fetched commits, creating a linear history.

### Resolving Conflicts During Synchronization

Conflicts may occur if changes in the remote repository overlap with your local changes. Git will mark the conflicting files, and you must resolve them before completing the synchronization.

### Best Practices

- Pull regularly to stay up-to-date.
- Push small, frequent commits to make collaboration easier.
- Communicate with your team to avoid overlapping work.
- Always resolve conflicts promptly and test after merging.

### Benefits

- Ensures everyone works with the latest code.
- Facilitates collaboration across distributed teams.
- Prevents code divergence and integration issues.
- Supports backup and recovery by storing code remotely.

```
```


## Make a Change

Making changes in Git involves editing files, staging those changes, committing them, and optionally sharing them with others. This workflow ensures that every modification is tracked and can be reviewed or reverted if needed.

### Editing Files

- Modify, add, or delete files in your working directory as needed.
- Git automatically detects changes to tracked files.

### Staging Changes

- Use `git add <file>` to stage specific files, or `git add .` to stage all changes.
- Staging allows you to control which changes are included in the next commit.

```bash
git add README.md           # Stage a single file
git add .                   # Stage all changes
```

### Committing Changes

- Use `git commit -m "Describe your change"` to save staged changes to the repository.
- Each commit should have a clear, descriptive message explaining the change.

```bash
git commit -m "Update documentation for installation"
```

### Reviewing Changes

- Use `git status` to see which files are modified, staged, or untracked.
- Use `git diff` to view unstaged changes, and `git diff --staged` for staged changes.

### Undoing Changes

- `git restore <file>`: Discards changes in the working directory.
- `git reset <file>`: Unstages a file from the staging area.
- `git commit --amend`: Updates the previous commit with new changes.

### Example Workflow

1. Edit files in your project.
2. Stage changes with `git add`.
3. Commit changes with `git commit`.
4. Push changes to a remote repository with `git push` (if collaborating).

### Best Practices

- Make small, focused commits for easier review and troubleshooting.
- Write clear commit messages.
- Review changes before committing.
- Test your changes before pushing to shared branches.

### Benefits

- Every change is tracked and can be reverted.
- Facilitates code review and collaboration.
- Maintains a clear project history.
- Supports experimentation and iterative development.

```
```


## Git Basics Summary

Git is a distributed version control system that enables efficient collaboration and tracking of changes in projects. The core workflow involves editing files, staging changes, committing them, and synchronizing with remote repositories.

### Key Areas

- **Basics:** Git tracks changes using repositories, commits, and branches. The workflow includes initializing/cloning repos, staging, committing, and reviewing history.
- **Branching & Merging:** Branches allow parallel development and isolation of features. Merging integrates changes, with conflict resolution when necessary. Best practices include keeping branches focused and deleting them after merging.
- **Synchronize:** Synchronization keeps your local repository up-to-date with remotes. Use `git fetch`, `git pull`, and `git push` to manage changes. Regularly pull and push to avoid conflicts and ensure collaboration.
- **Make a Change:** Edit files, stage changes, commit with descriptive messages, and push to share updates. Review and undo changes as needed. Small, clear commits help maintain project history and facilitate teamwork.

### Benefits

- Tracks every change and supports reverting.
- Enables collaboration and code review.
- Supports experimentation through branching.
- Maintains a clear, distributed project history.

This summary provides a quick reference to the essential concepts and workflows in Git for effective version control and team collaboration.

```
```



## Git Cheatsheet

### Basics
- `git init` — Initialize a new repository
- `git clone <url>` — Clone a remote repository
- `git status` — Show current changes
- `git add <file>` — Stage changes
- `git commit -m "message"` — Commit staged changes
- `git log` — View commit history

### Branching & Merging
- `git branch <name>` — Create a branch
- `git switch <name>` or `git checkout <name>` — Switch branches
- `git merge <name>` — Merge branch into current branch
- `git branch` — List branches
- Resolve conflicts: Edit files, `git add <file>`, `git commit`

### Synchronize
- `git remote add <name> <url>` — Add remote
- `git fetch <remote>` — Download changes
- `git pull <remote> <branch>` — Fetch and merge changes
- `git push <remote> <branch>` — Push commits to remote
- `git pull --rebase` — Reapply local commits on top of fetched commits

### Make a Change
- Edit files in working directory
- `git add <file>` or `git add .` — Stage changes
- `git commit -m "message"` — Commit changes
- `git push` — Share changes with remote
- `git status` — Review changes
- `git diff` — View unstaged changes
- `git restore <file>` — Discard changes
- `git reset <file>` — Unstage changes

### Best Practices
- Make small, focused commits
- Write clear commit messages
- Regularly pull and push
- Delete merged branches
- Resolve conflicts promptly

### Benefits
- Tracks every change
- Enables collaboration
- Supports branching and experimentation
- Maintains clear project history