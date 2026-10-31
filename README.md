---
title: Applied AI Engineering Student Labs
description: Staged original student challenges for Tecoholic and BITS Pilani Dubai Campus, 2026.
---

## Start Here

[Challenge 0: setup and readiness](labs/student/challenge-00-setup/README.md) is the initial release. Later student-facing challenges are published on their assigned teaching days. Instructor solutions, quizzes, slides, and licensed courseware are not distributed in this repository.

## Released Labs

These four hands-on labs were published on 31 October 2026. Complete them in the
order below. Google Lab 1 provides the key and JSON schema used by the next labs;
Google Lab 2 reuses the documents and evaluation set from Python Lab 1.

| Lab | Duration | Course slide |
|---|---|---|
| [Google Lab 1: Call Gemini from Python with a JSON response schema](labs/student/google-lab-01-json-schema/README.md) | 45 to 60 minutes | 90 |
| [AWS Lab 1: Free plan account, budget alert and Bedrock playground](labs/student/aws-lab-01-bedrock/README.md) | 45 to 60 minutes | 91 |
| [Python Lab 1: Cited RAG pipeline over public UAE policy documents](labs/student/python-lab-01-cited-rag/README.md) | 75 minutes, plus Part 2 in Week 2, Session 4 | 126 |
| [Google Lab 2: Gemini embeddings and File Search](labs/student/google-lab-02-embeddings-file-search/README.md) | 45 minutes | 141 |

Each lab has its own folder and full README instructions, viewable directly on
GitHub like Challenge 0. The folders contain course instructions, not your
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
Only these four practical labs are released; later labs remain unpublished.

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
