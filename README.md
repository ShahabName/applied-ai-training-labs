---
title: Applied AI Engineering Student Labs
description: Staged original student challenges for Tecoholic and BITS Pilani Dubai Campus, 2026.
---

## Start Here

[00-setup-lab: setup and readiness](labs/student/00-setup-lab/README.md) is the starting point. Later student-facing challenges are published on their assigned teaching days. Instructor solutions, quizzes, slides, and licensed courseware are not distributed in this repository.

## Released Labs

Complete 00-setup-lab first, then the appropriate provider setup. The four
practical labs were published on 31 October 2026. Start with the Google JSON
Schema lab before Bedrock or Python RAG; the File Search lab reuses the Python
RAG documents and evaluation set.

```text
labs/student/
├── 00-setup-lab/
├── images/
├── AWS/
│   ├── 00-AWS-Lab-Setup-AWS/
│   ├── 01-AWS-Lab-bedrock/
│   └── 02-AWS-Lab-RAG-Python/
└── Google-AI-Studio/
    ├── 00-GAIS-Lab-Setup-Google-Gemini/
    ├── 01-GAIS-Lab-JSON-Schema/
    └── 02-GAIS-Lab-Embedding-File-Search/
```

Every lab folder has a README. The existing combined HTML guide also remains
under `labs/student` for offline use.

| Lab | Duration | Course slide |
|---|---|---|
| [00-AWS-Lab-Setup-AWS](labs/student/AWS/00-AWS-Lab-Setup-AWS/README.md) | 45 minutes | Setup |
| [01-AWS-Lab-bedrock](labs/student/AWS/01-AWS-Lab-bedrock/README.md) | 45 to 60 minutes | 91 |
| [02-AWS-Lab-RAG-Python](labs/student/AWS/02-AWS-Lab-RAG-Python/README.md) | 75 minutes, plus Part 2 in Week 2, Session 4 | 126 |
| [00-GAIS-Lab-Setup-Google-Gemini](labs/student/Google-AI-Studio/00-GAIS-Lab-Setup-Google-Gemini/README.md) | 30 minutes | Setup |
| [01-GAIS-Lab-JSON-Schema](labs/student/Google-AI-Studio/01-GAIS-Lab-JSON-Schema/README.md) | 45 to 60 minutes | 90 |
| [02-GAIS-Lab-Embedding-File-Search](labs/student/Google-AI-Studio/02-GAIS-Lab-Embedding-File-Search/README.md) | 45 minutes | 141 |

The Python RAG exercise is grouped under AWS for course navigation, but its
existing implementation uses local embeddings and Gemini for answers. It is
not an AWS Bedrock RAG implementation.

Each lab has its own folder and full README instructions, viewable directly on
GitHub like 00-setup-lab. The folders contain course instructions, not your
completed portfolio: create the working folders specified in each lab in your
separate work/submission repository. Screenshots are shared under
`labs/student/images` and render in every lab README.

The [combined HTML guide](labs/student/released-labs.html) remains available for
offline viewing. GitHub displays its source rather than the formatted guide.
After cloning or pulling, open it in standalone Microsoft Edge. Keep the adjacent
`images` folder with the HTML file. No web server is needed. From the repository
root on Windows:

```powershell
Start-Process msedge -ArgumentList ('"' + (Resolve-Path .\labs\student\released-labs.html).Path + '"')
```

The guide includes numbered steps, code samples, screenshots, troubleshooting,
cleanup, and the source's testing notes. Those notes distinguish local tests from
API request checks with an invalid key; this publication is not a new live-cloud
test. Check current provider pricing, eligibility, model availability, and rate
limits before using your own account. Budget alerts do not cap spending.

These instructions are for your separate work/submission repository. Do not put
keys, account details, or your completed work into this distribution repository.
The two provider setup labs and four practical labs are released; later
practical labs remain unpublished.

## Course Schedule

Teaching: 21 September-14 November 2026. MBA recording/revision: Sundays through 15 November. Times and invitations come from the trainer. Azure practicals use the assigned Skillable Cloud Slice, not a student Azure subscription.

## Receive Updates

```powershell
git clone https://github.com/ShahabName/applied-ai-training-labs.git
Set-Location applied-ai-training-labs
git status --short
git pull --ff-only
```

Only pull when the materials clone is clean. If it is dirty or divergent, preserve your work and ask the trainer. Pull requests are for review, not downloading updates.

Keep your implementation in a separate work/submission repository. It may be public or private. A public fork cannot simply be made private. Invite GitHub username `shahabname` as a collaborator and share the repository URL through the approved college channel. Do not submit solutions to this public distribution repository.

## Safety

Use synthetic data. Never commit credentials, tokens, payment information, student personal data, or Skillable manuals. Cloud credits are conditional, not unlimited funding; budget alerts are not spending caps. Complete the offline readiness exercise before attempting any authorized live lab.
