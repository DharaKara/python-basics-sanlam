## Assignment

**1. Squash and Merge**:
   - **Description**: Squash and merge is a Git workflow where all the changes from a feature branch are condensed into a single commit before merging into the main branch.
   - **Process**:
     ```
     git checkout main
     git merge --squash feature-branch
     git commit -m "Squashed feature-branch changes"
     git push origin main
     ```
   - **Difference from Normal Merge**: Squash and merge condenses all the commits from the feature branch into a single commit before merging into the main branch. This helps keep the commit history cleaner and more organized.

**2. Rebase and Merge**:
   - **Description**: Rebase and merge is a Git workflow where the commits from the feature branch are moved to the tip of the main branch before merging, rewriting the commit history.
   - **Process**:
     ```
     git checkout feature-branch
     git rebase main
     git checkout main
     git merge feature-branch
     git push origin main
     ```
   - **Difference from Normal Merge**: Rebase and merge rewrites the commit history by moving the feature branch commits onto the tip of the main branch, resulting in a linear history without merge commits. This can make the history easier to understand and follow.

**3. Forks**:
   - **Definition**: A fork refers to a copy of a repository in a version control system, typically Git.
   - **Reasons for Using Forks**:
     - **Contributing to Open Source Projects**: Developers can propose changes to a project without directly altering the original repository.
     - **Experimenting with Modifications**: Forks enable developers to freely explore new features or modifications without impacting the original project.
     - **Customizing Existing Projects**: Developers can create personalized versions of existing projects tailored to specific needs using forks.
     - **Maintaining Separate Versions**: Forks can be used to maintain different versions of a project, such as a stable version for production and an experimental version for development.
     - **Backup and Preservation**: Forks serve as a backup mechanism, ensuring that a copy of the project is preserved even if the original repository is lost or deleted.
     
---