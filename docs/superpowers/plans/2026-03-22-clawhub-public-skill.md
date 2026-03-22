# Mdtero ClawHub Public Skill Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a clean public Mdtero skill package from `mdtero-public` so it can be released on ClawHub without exposing private implementation details.

**Architecture:** Keep the repository root as the public landing README and add a dedicated `skills/mdtero` publish directory containing the ClawHub-ready `SKILL.md`. Add a lightweight stdlib-based validation test so the public package can be checked locally before publish.

**Tech Stack:** Markdown, Python `unittest`, GitHub, ClawHub CLI

---

## Chunk 1: Repo Validation Skeleton

### Task 1: Add a failing validation test for the ClawHub package

**Files:**
- Create: `tests/test_clawhub_package.py`

- [ ] **Step 1: Write the failing test**

```python
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "mdtero" / "SKILL.md"


class ClawHubPackageTests(unittest.TestCase):
    def test_skill_bundle_exists(self):
        self.assertTrue(SKILL.exists())
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /Users/jianbinchen1/Library/CloudStorage/OneDrive-TheUniversityofNottingham/JONBIN_CORP_HQ/01_LITERATURE/mdtero-public && python3 -m unittest discover -s tests -v`
Expected: FAIL because `skills/mdtero/SKILL.md` does not exist yet

## Chunk 2: Public Skill Bundle

### Task 2: Add the public Mdtero ClawHub skill files

**Files:**
- Create: `skills/mdtero/SKILL.md`
- Modify: `README.md`

- [ ] **Step 1: Write minimal public skill bundle**

Include:
- public-safe Mdtero description
- OpenClaw-focused usage guidance
- explicit `MDTERO_API_KEY` requirement
- explicit `PDF is optional input`
- explicit local-helper / browser-extension boundary for Elsevier and ScienceDirect
- public API endpoints for parse, translate, status, and downloads

- [ ] **Step 2: Update root README**

Include:
- repo now contains the public ClawHub skill bundle
- local validation command
- exact publish path and release command pattern

## Chunk 3: Validate and Hand Off Publish

### Task 3: Expand validation and run it green

**Files:**
- Modify: `tests/test_clawhub_package.py`

- [ ] **Step 1: Check frontmatter and required copy**

Assert that:
- `SKILL.md` has frontmatter with `name` and `description`
- it references `MDTERO_API_KEY`
- it references `POST /tasks/parse`
- it references `POST /tasks/translate`
- it references `paper_md`
- it references `translated_md`
- it states that PDF is optional input

- [ ] **Step 2: Run tests to verify they pass**

Run: `cd /Users/jianbinchen1/Library/CloudStorage/OneDrive-TheUniversityofNottingham/JONBIN_CORP_HQ/01_LITERATURE/mdtero-public && python3 -m unittest discover -s tests -v`
Expected: PASS

### Task 4: Prepare publish handoff

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Record final publish commands**

Include:
- `clawhub login`
- `clawhub publish ./skills/mdtero --slug mdtero --name "Mdtero" --version <version> --tags latest`

- [ ] **Step 2: Verify git status before user handoff**

Run: `git status --short`
Expected: only intended public skill repo files changed
