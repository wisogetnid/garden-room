Execute each research area in parallel with the research context passed in. For each task, spawn a sub-session and execute following process.

    Branch: Create and switch to a new branch named research/[topic-name].

    Research: Perform deep research on the topic.

    Write: Save the findings to research/[topic-name].md.

    Commit: Stage the file and commit with message: 'feat: add deep research for [topic]'.

    Push & PR: Push the branch to origin and use gh pr create --fill to open a Pull Request to main.
