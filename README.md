# Mdtero

Mdtero turns papers into reusable Markdown research packages for reading, translation, and downstream agent work.

This repository is the lightweight public entry point and public skill source for Mdtero. It intentionally does **not** contain the active website workspace, the active extension workspace, or the private backend implementation.

## Repo Role

Use this repo for:

- the public OpenClaw / ClawHub skill
- lightweight public product messaging
- simple public packaging tests

Do not use this repo as the source of truth for:

- website, dashboard, or account behavior
- browser extension behavior
- backend auth, billing, parsing, or deployment logic

Current ownership:

- active product workspace: [JonbinC/mdtero](https://github.com/JonbinC/mdtero)
- extension mirror and sideload repo: [JonbinC/Mdtero-Extension](https://github.com/JonbinC/Mdtero-Extension)
- backend deploy and private service SSOT: `JonbinC/mdtero-backend`

## Product Entry

- Website: [mdtero.com](https://mdtero.com)
- Demo: [mdtero.com/demo](https://mdtero.com/demo)
- Account: [mdtero.com/account](https://mdtero.com/account)
- API docs: [mdtero.com/api](https://mdtero.com/api)

## Start here

- Account: [mdtero.com/account](https://mdtero.com/account)
- Guide: [mdtero.com/guide](https://mdtero.com/guide)
- Demo: [mdtero.com/demo](https://mdtero.com/demo)
- OpenClaw: `clawhub install mdtero`
- Chrome Web Store: [Mdtero on Google Chrome](https://chromewebstore.google.com/detail/mdtero/knpihhcooldgedbklgjghebijcpejibp)
- Edge Add-ons: [Mdtero on Microsoft Edge](https://microsoftedge.microsoft.com/addons/detail/mdtero/bgikfidgigjnkgfdhhopojgpckilknic)

Required environment variables for agent and API usage:

- `MDTERO_API_KEY` for Mdtero API authentication
- `ELSEVIER_API_KEY` only when the user wants Elsevier or ScienceDirect full-text retrieval

For the local helper, download the installer, inspect it, then run it. Do not pipe a remote script directly into the shell.

The public API remains task-based:

- `POST /tasks/parse` returns `task_id`
- `POST /tasks/translate` returns `task_id`
- `GET /tasks/{task_id}` is the stable completion contract
- `mdtero-local parse` and `mdtero-local translate` are the convenience layer that short-waits by default and may print the completed task payload directly

## ClawHub Skill

The public OpenClaw skill bundle lives at:

- `skills/mdtero/SKILL.md`

This skill keeps the public surface focused on:

- `POST /tasks/parse` for structured paper parsing
- `POST /tasks/translate` for aligned translation on top of `paper_md`
- `GET /tasks/{task_id}` for status checks
- download routes for `paper_md`, `paper_bundle`, optional `paper_pdf`, and `translated_md`

Validation:

```bash
python3 -m unittest discover -s tests -v
```

Publish flow:

```bash
clawhub login
clawhub --workdir . publish skills/mdtero --slug mdtero --name "Mdtero" --version <version> --tags latest
```

## What Mdtero Does

- Turn a DOI, paper page, or local file into `paper.md` and a reusable bundle
- Keep figures and downloadable artifacts with the same paper structure
- Produce aligned translation outputs for research reading
- Hand clean paper packages off to agents and downstream workflows

## Product Boundary

- This repository is public-facing only
- Core application code, backend logic, infrastructure, and private workflows stay in private repositories
- Publisher-side acquisition that requires local handling remains on the user's side through the extension or local helper
- If wording here conflicts with the active product repo, `JonbinC/mdtero` is authoritative for current product behavior

## Public Repositories

- Product skill repo: this repository
- Product workspace and frontend SSOT: [JonbinC/mdtero](https://github.com/JonbinC/mdtero)
- Browser extension repo: [JonbinC/Mdtero-Extension](https://github.com/JonbinC/Mdtero-Extension)

## Contact

- Support: [support@mdtero.com](mailto:support@mdtero.com)
