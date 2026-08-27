# Antigravity setup

This folder is prepared as a single-folder Antigravity Project.

## Create the Project

1. Open Antigravity.
2. Click the folder-with-plus control in the left sidebar.
3. Choose **New Project**.
4. Choose **Add Folder**.
5. Select the extracted folder `GraphSSL_KT_Survey_2026`.
6. Create the Project.
7. Start in **Local Mode** for sequential pilot work.
8. Read/paste `ANTIGRAVITY_FIRST_PROMPT.md`.

## Project customizations included

### Root agent guidance
`AGENTS.md`

### Workspace rules
`.agents/rules/`

### Workspace custom agents
`.agents/agents/<agent-name>/agent.md`

### Workspace skills
`.agents/skills/<skill-name>/SKILL.md`

### Workflow source files
`workflows_for_import/`

The workflow Markdown files are included as source specifications. Register them through Antigravity's Customizations → Workflows panel if you want slash-command workflows.

## Recommended mode

Use **Local Mode** while the codebook is still changing so all agents see the same evolving files.

Use isolated worktrees only later for independent code changes or parallel scripts that should not touch the same coding artifacts.

## Security

For research artifacts, keep terminal/write actions reviewable. Do not grant a browsing/coding agent permission to delete or overwrite locked evidence files automatically.
