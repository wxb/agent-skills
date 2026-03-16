---
name: git-conventional-commits
description: Generates a git commit message following the Conventional Commits specification by analyzing staged changes. Use this skill when the user wants to commit code, generate a commit message, or standardize a commit.
---

# Git Conventional Commits Skill

This skill enables the AI to generate high-quality, standardized git commit messages based on the current staged changes. It adheres to the [Conventional Commits](https://www.conventionalcommits.org/) specification and supports [Gitmoji](https://gitmoji.dev/).

## Workflow

When triggered, follow these steps:

1.  **Check Status**:
    -   Run `git status` to check for staged changes.
    -   If no changes are staged but modified files exist, ask the user if they want to stage all changes (`git add .`) or specific files.
    -   If no changes exist, inform the user.

2.  **Analyze Diff**:
    -   Run `git diff --cached` to get the content of the staged changes.
    -   Analyze the diff to understand the intent and scope of the changes.
    -   Identify the primary **type** (feat, fix, etc.) using `references/types.md`.
    -   Identify the **scope** (e.g., module name, file name).
    -   Select a relevant **emoji** using `references/emojis.md`.

3.  **Generate Message**:
    -   Construct the commit message using the following format:
        ```
        <type>(<scope>): <emoji> <subject>

        <body>

        <footer>
        ```
    -   **Header**:
        -   `<type>`: Must be one of the types in `references/types.md`.
        -   `(<scope>)`: Optional but recommended.
        -   `<emoji>`: Select from `references/emojis.md`.
        -   `<subject>`: Imperative, present tense (e.g., "add feature" not "added feature").
    -   **Body** (Optional):
        -   Use for non-trivial changes.
        -   Use bullet points (`- `) for multiple changes.
        -   Explain *what* and *why*.
    -   **Footer** (Optional):
        -   Reference issues (e.g., `Closes #123`).
        -   Mention breaking changes (`BREAKING CHANGE: ...`).

4.  **Review & Output**:
    -   Present the generated commit message to the user for review.
    -   (Optional) You can run `python scripts/validate.py "<message>"` to verify the format before presenting.
    -   Ask the user if they want to proceed with the commit (`git commit -m "..."`).

## Examples

### Feature with Scope and Body
**Input**: Added a new login function in `auth.py` and updated the user model.
**Output**:
```
feat(auth): ✨ Add user login functionality

- Implemented `login` function in `auth.py`
- Updated `User` model to support session tokens
```

### Bug Fix
**Input**: Fixed a crash when input is null in `parser.js`.
**Output**:
```
fix(parser): 🐛 Handle null input in parser

- Added check for null input to prevent runtime error
- Added unit test for null case
Closes #42
```

### Documentation
**Input**: Updated README with installation instructions.
**Output**:
```
docs(readme): 📝 Update installation instructions
```

## References

-   [Commit Types](references/types.md)
-   [Gitmojis](references/emojis.md)
