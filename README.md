# Mdtero

Mdtero is an AI-ready research pre-processing workflow for paper capture, parsing, translation, and agent handoff.

This public repository is a lightweight product entry point and the public ClawHub skill source for Mdtero. It intentionally does **not** contain the private application or backend implementation.

## Product Entry

- Website: [mdtero.com](https://mdtero.com)
- Demo: [mdtero.com/demo](https://mdtero.com/demo)
- Account: [mdtero.com/account](https://mdtero.com/account)
- API docs: [mdtero.com/api](https://mdtero.com/api)

## Install

- Edge Add-ons: [Mdtero on Microsoft Edge](https://microsoftedge.microsoft.com/addons/detail/mdtero/bgikfidgigjnkgfdhhopojgpckilknic)
- Direct extension ZIP: [mdtero.com/assets/mdtero-extension-beta.zip](https://mdtero.com/assets/mdtero-extension-beta.zip)
- Agent install guide: [api.mdtero.com/skills/install.md](https://api.mdtero.com/skills/install.md)
- Local helper install script: [api.mdtero.com/helpers/install_mdtero_helper.sh](https://api.mdtero.com/helpers/install_mdtero_helper.sh)

## ClawHub Skill

The public OpenClaw skill bundle lives at:

- `skills/mdtero/SKILL.md`

This skill keeps the public surface focused on:

- `POST /tasks/parse` for structured paper parsing
- `POST /tasks/translate` for aligned translation on top of `paper_md`
- `GET /tasks/{task_id}` for status checks
- download routes for `paper_md`, `paper_bundle`, and `translated_md`

Validation:

```bash
python3 -m unittest discover -s tests -v
```

Publish flow:

```bash
clawhub login
clawhub publish ./skills/mdtero --slug mdtero --name "Mdtero" --version 0.1.0 --tags latest
```

## What Mdtero Does

- Capture supported papers from the browser or local helper flow
- Convert papers into structured Markdown packages with figures and artifacts
- Produce aligned translation outputs for research reading
- Hand off clean paper packages into agents and downstream workflows

## Product Boundary

- This repository is public-facing only
- Core application code, backend logic, infrastructure, and private workflows stay in private repositories
- Publisher-side acquisition that requires local handling remains on the user's side through the extension or local helper

## Public Repositories

- Product entry repo: this repository
- Browser extension repo: [JonbinC/Mdtero-Extension](https://github.com/JonbinC/Mdtero-Extension)

## Contact

- Support: [support@mdtero.com](mailto:support@mdtero.com)
