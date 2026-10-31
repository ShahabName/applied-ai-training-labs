---
title: "00-Python-Lab-Setup-Python"
description: Prepare an isolated Python environment and verify offline readiness for Python labs.
id: P00
cloud: Local Python; no cloud account required
difficulty: Foundation
release_date: 2026-10-31
estimated_minutes: 30
dependencies: [CH00]
---

## Start here

[All student labs](../../../../README.md) |
[General setup](../../00-Setup-Lab/README.md) |
[Next: 01-Python-Lab-RAG](../01-Python-Lab-RAG/README.md)

Prepare your separate work/submission repository for local Python exercises.
This lab needs no API key, paid service, model download or cloud account.
The RAG lab's retrieval and evaluation run locally; its optional answer step
requires Gemini access from the Google AI Studio labs.

## Prerequisites

1. Complete the Git and separate-repository checks in 00-Setup-Lab.
2. Install Python 3.12 or 3.13, Git, VS Code with its Python extension, and
   [uv](https://docs.astral.sh/uv/getting-started/installation/).
   Python 3.14 is supported by the historical readiness check, but later
   optional packages may not provide compatible wheels.
3. Apply the [general setup ignore rules](../../00-Setup-Lab/.gitignore) to
   your work repository. Ignore `.venv/`, `.env`, `.env.*`, caches and
   credentials. Do not overwrite existing ignore rules.
4. Use synthetic data for exercises. Keep your work out of the public materials
   repository.

## Create an isolated environment

In your separate work repository, run:

```powershell
git --version
py -3.13 --version
code --version
uv --version
uv venv .venv --python 3.13
.\.venv\Scripts\python.exe --version
```

If uv is unavailable, use `py -3.13 -m venv .venv` instead.
Activation is optional: invoking the environment's executable avoids
PowerShell activation-policy problems. Do not disable execution policy or TLS
verification to fix an installation issue.

In VS Code, use Python: Select Interpreter to select this `.venv`.
On macOS/Linux, use `.venv/bin/python` rather than the Windows executable path.

## Run the offline readiness checkpoint

From the root of your clean course materials clone, run the existing setup
script using your work repository's environment:

```powershell
$python = 'C:\path\to\your-work-repository\.venv\Scripts\python.exe'
& $python -I -B .\labs\student\00-Setup-Lab\readiness.py --offline
```

Replace the example path with your actual environment executable. The script
uses only the standard library and an in-memory SQLite database; no package
installation or network access is needed.

Expected fields include:

```json
{
  "status": "local_readiness_passed",
  "mode": "offline",
  "synthetic_rows": 2,
  "cloud_calls": 0,
  "cloud_eligibility_verified": false
}
```

The actual output also contains your Python and SQLite versions and optional
package availability. Missing optional packages are informative, not failures.
Do not present this output as a successful cloud test.

## Prepare for the RAG lab

1. Create `week2/rag/data` in your separate work repository.
2. Follow 01-Python-Lab-RAG to create its own environment and install the
   documented packages. Do not install them merely to pass this setup.
3. Download only the public documents linked in that lab and preserve attribution.
4. Start with retrieval-only and evaluation. These need no Gemini key, but the
   first embedding-model download needs a network connection and disk space.
5. For answer generation, separately complete Google AI Studio setup and the
   JSON Schema lab. Never put a real key in code, screenshots or commits.

## Acceptance and troubleshooting

Record interpreter versions, successful sanitized readiness output, the selected
environment and your separate work repository URL. Explain why parameterized
SQL is used in the readiness exercise. Do not submit environment dumps,
credentials or personal data.

* Python not found: reopen the terminal and verify the installed launcher.
* Script asks for a virtual environment: use the `.venv` executable, not system Python.
* Import unavailable in later labs: check the selected interpreter and install
  only the packages required by that lab.
* Corporate certificate errors: use an institution-approved mirror and
  certificates; never bypass TLS verification.

## Cleanup and validation limits

No cloud resource is created. Close terminals when finished and retain the
environment for your work as appropriate. Never delete shared accounts,
repositories or billing resources as part of local cleanup.

This lab adapts the general setup's existing offline readiness exercise. It
does not claim a newly executed model or cloud API test.
