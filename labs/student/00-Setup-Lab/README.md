---
title: 00-Setup-Lab - Setup and Readiness
description: Self-contained local readiness, safe GitHub workflow, and conditional cloud access without student Azure signup.
id: CH00
cloud: Neutral; Azure via Skillable only
difficulty: Foundation
release_day: D01
release_date: 2026-09-21
estimated_minutes: 60
objectives: [O01, O02, O13]
dependencies: []
---

## What you will learn

### What we will do

Prepare a reproducible workspace, run a small offline database exercise, and
separate the course materials clone from your own work repository. Review
cloud-access, credential and cost boundaries before any live exercise.

### Libraries and tools

Use Python's standard-library `sqlite3`, `json`, `argparse` and
`importlib.metadata`, plus Git, uv and VS Code. No third-party Python package
or cloud SDK is required; the script only checks optional package availability.

### Important calls and commands

`sqlite3.connect(":memory:")` creates a temporary database;
`executemany(..., parameters)` inserts synthetic tickets using SQL parameters;
`execute(...).fetchall()` retrieves them. `json.dumps()` formats the evidence.
`git status --short` checks for local changes and `git pull --ff-only` downloads
releases without creating a merge commit.

### Expected results

The readiness output reports `local_readiness_passed`, two synthetic rows and
zero cloud calls. You also have an isolated interpreter, a separate work
repository and an honest eligible/pending/offline access checklist.

### Connection to agentic AI

Agents need predictable runtimes, safe data access and explicit permissions.
Parameterized SQL, reproducibility and sanitized evidence are foundations for
later agent tools. This setup does not build or run an autonomous agent.

## Mission and Prerequisites

[All student labs](../../../README.md) |
[Python setup](../01-Python/00-Python-Lab-Setup-Python/README.md) |
[AWS setup](../03-AWS/00-AWS-Lab-Setup-AWS/README.md) |
[Google AI Studio setup](../02-Google-AI-Studio/00-GAIS-Lab-Setup-Google-Gemini/README.md)

Prepare a reproducible workspace for the Service Operations Copilot portfolio using invented retailer tickets. Complete this readiness gate before the four required cloud challenges. No model, paid service, shared helper, or later challenge is required here. You need a supported laptop, permission to install development tools, your college identity for the course, and a personal GitHub account. A credit offer is not an eligibility guarantee.

Choose foundation or stretch dataset difficulty later, but complete every required objective in all four cloud challenges. Offline evidence is accepted when access is unavailable, provided it is labelled offline. Do not present replay as a successful cloud test.

## Local Tools and 20-Minute Checkpoint

Use Python 3.12 or 3.13, Git 2.40+, current VS Code, and current external Microsoft Edge. The trainer tested this self-contained check on Python 3.14.7/Windows x64. Optional wheels can lag new Python releases, so 3.14 is not the student default. Install Docker Desktop with WSL2/Linux-container support before Week 4, subject to institutional permissions and Docker licensing. Docker is not needed to pass Challenge 0.

Download from the official [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/downloads), [VS Code](https://code.visualstudio.com/Download), [uv](https://docs.astral.sh/uv/getting-started/installation/), and [Docker](https://docs.docker.com/desktop/setup/install/windows-install/) pages. Run in your materials clone:

```powershell
git --version
py -3.13 --version
code --version
uv --version
uv venv .venv --python 3.13
.\.venv\Scripts\python.exe -I -B labs/student/00-Setup-Lab/readiness.py --offline
```

If `uv` is unavailable, `py -3.13 -m venv .venv` creates the same environment with the standard library. On macOS/Linux use `python3.13 -m venv .venv` and `.venv/bin/python`. Select that environment with VS Code's Python: Select Interpreter. Activation is optional when using the explicit executable. No package install is required for this exercise.

[readiness.py](readiness.py) verifies an in-memory SQLite query, JSON serialization and the virtual environment. Expected output includes `local_readiness_passed`, `synthetic_rows: 2`, `cloud_calls: 0`, and your actual Python version. Missing later packages are informative, not readiness failures. This is not proof of cloud entitlement. Keep the local output and explain why SQL parameters are preferable to concatenating untrusted text.

If Python is not found, reopen your terminal after installation and check the launcher version. An execution-policy error is avoided by calling the interpreter directly; do not disable security controls globally. Later labs install public packages from [PyPI](https://pypi.org/), whose standard package index is `https://pypi.org/simple/`. pip uses this index by default unless your environment configures another one. No package installation is needed for this readiness check. If your institution requires an approved HTTPS mirror or certificates, follow its guidance. Never use `--trusted-host`, insecure TLS flags, or copied credentials to bypass a failure.

## GitHub and 15-Minute Checkpoint

The verified public materials repository is <https://github.com/ShahabName/applied-ai-training-labs>. Initially the public tree contains only this Challenge 0 directory and minimal navigation. Trainer references, later labs, slides and answer keys must never be copied into that public history.

```powershell
$materialsUrl = 'https://github.com/ShahabName/applied-ai-training-labs.git'
git clone $materialsUrl course-materials
Set-Location course-materials
git status --short
```

Create a separate personal work/submission repository and clone it separately. Choose public only for work you intend to share; choose private for privacy. A fork of a public repository remains public and cannot simply be made private. An independent private repository avoids this limitation. Copy only your assigned starter and allowed original fixtures into your work repository. Keep all course materials under their released relative layout when a shared helper is needed. Never push student answers into the public distribution repository.

Use Settings > Collaborators > Add people in your work repository, select `shahabname`, verify the profile, and send the invitation. Share your work repository URL through the approved college channel. Invitation acceptance must be confirmed separately. The supplied email `shahab,name@gmail.com` contains a comma and is unverified; do not silently fix it or use it for invitations.

To receive new releases, keep the materials clone clean:

```powershell
git status --short
git pull --ff-only
```

Run `git pull --ff-only` only if status is empty and this is the intended materials clone. If dirty or divergent, stop, preserve your work, and ask the trainer; do not reset or force-push. This does not update your separate work repository automatically. Pull requests submit changes for review; they do not download daily labs. Use a small work-repository commit and reviewed pull request as your engineering evidence.

## Skillable and 10-Minute Checkpoint

Use the supplied [AI-103 Cloud Slice](https://msft-ilt.skillable.com/ai-103t00-a-develop-ai-apps-and-agents-on-azure-cloud-slice-provided/) entitlement. Students must not sign up for an Azure subscription or obtain an Azure Pass. The trainer supplies the exact portal, training key or existing enrollment. Use Create/Register with Training Key if new, otherwise sign in to the existing account and redeem once. Open Current/My Training, the class, Activities, then Launch after enrollment is active and the class has started. Azure credentials shown inside the lab are distinct from your Skillable sign-in.

The public listing allows at most 10 launches per lab. Confirm your actual remaining count, timer and training expiry before every launch. Cloud Slice has no save/resume; a generic Skillable Save and Close instruction does not apply. Closing Edge is not suspension. Do not relaunch repeatedly as a troubleshooting tactic.

Every Azure practical is a fresh instance with this exact 90-minute budget:

| Block | Minutes | Required result |
| --- | --- | --- |
| Fresh launch and access check | 10 | Check entitlement, timer, identity, permitted resource/region/model boundary |
| Entitled provider task | 45 | Follow only the authorized current manual inside Skillable |
| Failure and trace analysis | 20 | Explain one redacted permission, quota or response observation |
| Approved export and cleanup | 15 | Export allowed student-authored code, placeholder configuration and sanitized results; end the instance |

Reconstruct from approved student code in each new launch. Do not carry credentials, resource state, proprietary manuals, provider answers or lab keys between sessions. On D24, only fresh provider-managed initialization is allowed, not arbitrary infrastructure. If the timer or entitlement prevents reconstruction, use explicitly labelled provider-shaped replay and mark live verification unavailable.

For missing Launch, check enrollment, class start, code spelling, expiry and attempts first. Use external Edge and site-scoped pop-up/cookie exceptions, not disabled browser security. Ask campus IT about required secure WebSocket connectivity on 443. Escalate using a redacted lab instance ID/error, never a credential screenshot. Do not change region or substitute a personal Azure account to escape quota restrictions.

## Conditional GCP and AWS Access

This is a private checklist, not authorization to create resources today. No student must buy access to pass the course. Only the account owner completes consent, payment and identity verification in their own browser; credentials never enter chat or evidence.

| Gate | GCP | AWS |
| --- | --- | --- |
| Offer checked 2026-09-21 | Eligible new customers: USD 300 for 90 days; use console's exact expiry | Eligible new customers: USD 100 at signup plus up to USD 100 earned; extra credits not required |
| Eligibility | No previous trial or paying GCP/Maps/Firebase use; contractual capacity and authentic country details | No existing/former AWS customer; contractual capacity; participating commercial regions, not China/GovCloud |
| Payment | Valid supported payment instrument and identity verification; country-dependent | Standalone route requires payment and identity/phone checks; India has additional verification and refundable INR 2 card check |
| Expiry | Trial exhaustion/expiry stops access without automatic Paid upgrade | Free Plan ends at six months or credit exhaustion; credits' twelve-month expiry is a different clock |
| Service route | Cloud project and `aiplatform.googleapis.com`, not Gemini Developer API/AI Studio credits | Bedrock Runtime; first-party Nova only; no Marketplace model subscription |
| Model/region later | `gemini-3.1-flash-lite`, `global`; global is not a residency promise | Micro/Lite direct models in `us-east-1`; no automatic cross-region profile |
| Runtime permission | `aiplatform.endpoints.predict`; documented `roles/aiplatform.user` is a starting role, not Owner | `bedrock:InvokeModel` on the exact approved model ARN; no invented `bedrock:Converse` IAM action |

GCP activation: privately verify eligibility, open the official Cloud Free Trial, confirm Free trial account and remaining credit, then use an isolated approved project. Enabling `aiplatform.googleapis.com` is different from activating Paid billing. Do not click Upgrade/Activate, select a paid billing account or configure auto-reload. The USD 300 does not fund the Gemini Developer API/AI Studio or partner managed model APIs. Use the cloud SDK backend with ADC only after the trainer's access gate; do not paste an AI Studio key into a cloud-project exercise.

AWS activation: choose the qualifying standalone Free Plan and Basic support when offered, verify credit/expiry, and later use a non-root temporary session/profile. Never create/join an Organization or activate auto-upgrade programs to fix access. A limited new AWS signup experience manages Organizations and region controls differently; stop and ask the trainer if your screen differs, rather than converting it to advanced/Paid mode. Published Bedrock availability does not guarantee a particular model in your account.

Set an illustrative USD 1 gross-cost budget with actual alerts at USD 0.50/0.80/1.00, excluding credits from gross monitoring; inspect remaining credit separately. Budget alerts are delayed notifications, not spending caps. Later labs enforce 50 total generation attempts per cloud across both labs, counting failures; no unbounded retries. At 1,000 input and 200 billable output tokens each, 50 calls are approximately USD 0.0275 GCP or USD 0.0054 if all AWS calls use Nova Lite, before tax, thinking, rounding and other services. These are assumptions, not account spending ceilings. Cloud access is not exercised by readiness.py.

## Acceptance, Evidence and Rubric

Complete a 15-minute self-review: record your tool versions, successful offline JSON, sanitized Git workflow, work repository URL/collaborator invitation state, and an access matrix marked eligible, pending or offline for each provider. Do not submit account IDs, payment details, environment dumps, `.env` contents, keys, tokens or lab credentials. Use the supplied [.gitignore](.gitignore) rules in your work repository as well as the material directory.

| Criterion | Points | Observable acceptance |
| --- | --- | --- |
| Local tools and data exercise | 30 | Correct isolated interpreter, two SQL rows, zero network |
| Safe GitHub workflow | 25 | Separate work repository, clean-clone update explained, `shahabname` invitation state |
| Access and billing understanding | 25 | Conditional offers, no Azure signup, fresh Cloud Slice launch, alerts are not caps |
| Evidence hygiene | 20 | Sanitized evidence and limitations; no credentials or personal data |

Pass: at least 70/100 and all safety gates. A credentials leak or unauthorized paid upgrade requires remediation regardless of score. Cloud ineligibility is not a penalty when documented with offline completion.

## Cleanup and Optional Extension

End any authorized Skillable instance after approved export. Close local processes. Do not delete shared institutional identities or billing accounts. No cloud resource is created by the readiness exercise. Inspect billing and task-owned resources after any later authorized cloud use; eventual trial expiry is not cleanup.

Optional: repeat the stdlib check on a second OS or use a synthetic dataset variant. This adds no required objective and should cost zero. Do not add hosted notebooks, databases, model endpoints, GPU VMs or paid upgrades for readiness.

## Official Sources

Public documentation checked 2026-09-21; actual entitlement, geography/payment eligibility and account controls remain learner-specific.

* [GitHub fork permissions and visibility](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks), [collaborator invitations](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository), and [git pull](https://git-scm.com/docs/git-pull)
* [Skillable Cloud Slice policy](https://www.skillable.com/courseware/moc/moc-cloud-slice/), [redeem codes](https://docs.skillable.com/docs/how-do-i-access-labs-by-redeeming-lab-codes.md), [access classes](https://docs.skillable.com/docs/how-and-when-do-learners-get-access.md), [launch limits](https://docs.skillable.com/docs/understanding-course-lab-access-expiration-and-launch-limits.md), and [connectivity](https://docs.skillable.com/docs/lab-connectivity-requirements.md)
* [Google trial and exclusions](https://docs.cloud.google.com/free/docs/free-cloud-features), [terms](https://cloud.google.com/terms/free-trial), [budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets), [cloud authentication](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/gcp-auth), and [cloud pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)
* [AWS account plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html), [credit terms](https://aws.amazon.com/free/terms/), [signup](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html), [Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), [model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html), and [pricing](https://aws.amazon.com/bedrock/pricing/)
