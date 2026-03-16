# Agent Skills


## Git Conventional Commits Skill

This repository contains an AI Skill designed to help intelligent agents generate standardized git commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Features

-   **Automatic Analysis**: Inspects staged changes using `git diff`.
-   **Standardized Format**: Generates messages in the format `<type>(<scope>): <emoji> <subject>`.
-   **Gitmoji Support**: Includes relevant emojis for visual clarity.
-   **Validation**: Includes a script to validate commit messages against the specification.

### Project Structure

```
git-conventional-commits-skill/
├── git-conventional-commits/       # The skill package
│   ├── SKILL.md                    # Main skill definition and instructions
│   ├── references/                 # Reference data for the AI
│   │   ├── types.md                # List of conventional commit types
│   │   └── emojis.md               # List of supported gitmojis
│   └── scripts/                    # Helper scripts
│       └── validate.py             # Script to validate commit message format
├── .gitignore
└── README.md
```

### Usage

1.  **Installation**: Point your AI agent or IDE to the `git-conventional-commits` directory.
2.  **Trigger**: Ask the agent to "commit changes", "generate a commit message", or "create a commit".
3.  **Workflow**:
    -   The agent will check for staged changes.
    -   If changes are staged, it will analyze them.
    -   It will generate a commit message with a type, scope, emoji, subject, and optional body/footer.
    -   It will present the message for your review.

### Customization

-   **Types**: Edit `git-conventional-commits/references/types.md` to add or remove commit types.
-   **Emojis**: Edit `git-conventional-commits/references/emojis.md` to change the emoji set.
-   **Validation**: Modify `git-conventional-commits/scripts/validate.py` to adjust validation rules.

### References

-   [Conventional Commits](https://www.conventionalcommits.org/)
-   [Gitmoji](https://gitmoji.dev/)
