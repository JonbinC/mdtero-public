---
name: mdtero
description: Parse papers into structured Markdown research packages and optionally translate them for OpenClaw workflows.
---

# Mdtero

Use Mdtero to turn one paper into a structured Markdown research package for downstream OpenClaw work.

## When To Use

Use this skill when the user wants to:

- parse a paper from a DOI, supported publisher page, or open URL into a Markdown research package
- translate an already parsed paper without losing the original research structure
- check task status and download `paper_md`, `paper_bundle`, or `translated_md`

## Required Setup

1. Check whether `MDTERO_API_KEY` is already available.
2. If it is missing, tell the user to generate one at `https://mdtero.com/account`.
3. Ask them to export it locally:

```bash
export MDTERO_API_KEY="mdt_live_..."
```

4. Authenticate requests with:

```bash
Authorization: ApiKey $MDTERO_API_KEY
```

5. If the user wants Elsevier or ScienceDirect full-text retrieval, also check `ELSEVIER_API_KEY` and explain that it is separate from `MDTERO_API_KEY`.
6. If an Elsevier DOI is missing the local helper or `ELSEVIER_API_KEY`, tell the user exactly what is missing instead of guessing.

## Workflow Rules You Must Preserve

- PDF is optional input. Prefer the Markdown package first and only fall back to PDF when the workflow truly requires it.
- For Elsevier and ScienceDirect, local acquisition should stay on the user's own machine through the local helper or browser extension.
- If an Elsevier parse only returns the abstract, ask whether the user is on a campus or institutional IP.
- For Elsevier papers, prefer the raw DOI form such as `10.1016/j.energy.2026.140192`.

## Local Helper

When the user needs local acquisition for Elsevier or ScienceDirect, tell them to download it, review it, then run it:

```bash
curl -fsSL https://api.mdtero.com/helpers/install_mdtero_helper.sh -o install_mdtero_helper.sh
sed -n '1,160p' install_mdtero_helper.sh
chmod +x install_mdtero_helper.sh
./install_mdtero_helper.sh
```

Explain that the installer auto-detects `python3`, `python`, or `node`, and does not require extra packages. Do not recommend piping a remote script directly into the shell.

## Parse A Paper

Open inputs can go directly to `POST /tasks/parse`.

```bash
mdtero-local parse "10.1016/j.enconman.2026.121230"

curl -X POST https://api.mdtero.com/tasks/parse \
  -H "Authorization: ApiKey $MDTERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input": "https://arxiv.org/abs/1706.03762"}'
```

The response returns a `task_id`.

## Translate A Parsed Markdown File

Use `POST /tasks/translate` with the server-side Markdown artifact path returned by a succeeded parse task in `result.artifacts.paper_md.path`. Do not substitute an arbitrary local file path.

```bash
  curl -X POST https://api.mdtero.com/tasks/translate \
  -H "Authorization: ApiKey $MDTERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "source_markdown_path": "<path from result.artifacts.paper_md.path>",
    "target_language": "zh",
    "mode": "standard"
  }'
```

The response returns a `task_id`. Poll it, then download `translated_md`.

## Check Task Status

Poll `GET /tasks/{task_id}` until the task becomes `succeeded`.

```bash
mdtero-local status <TASK_ID>

curl https://api.mdtero.com/tasks/<TASK_ID> \
  -H "Authorization: ApiKey $MDTERO_API_KEY"
```

The `result` object returns artifact metadata rather than the file body.

## Download Artifacts

Download file contents from the download route.

```bash
mdtero-local download <TASK_ID> paper_bundle ./paper_bundle.zip

curl -L https://api.mdtero.com/tasks/<TASK_ID>/download/paper_md \
  -H "Authorization: ApiKey $MDTERO_API_KEY" \
  -o paper.md

curl -L https://api.mdtero.com/tasks/<TASK_ID>/download/translated_md \
  -H "Authorization: ApiKey $MDTERO_API_KEY" \
  -o paper.zh.md
```
