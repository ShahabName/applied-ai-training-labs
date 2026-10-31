---
title: "01a-AWS-Lab-Bedrock-BedTimeStory"
description: Generate a one-sentence story through Amazon Bedrock using the OpenAI-compatible Responses API.
id: A01a
cloud: AWS Amazon Bedrock
difficulty: Foundation
release_date: 2026-10-31
estimated_minutes: 20
dependencies: [CH00, A00, A01]
---

## What you will learn

### What we will do

Configure the OpenAI Python SDK to call Amazon Bedrock, submit a short
creative-writing prompt and inspect the returned text. Keep the Bedrock key
private and verify the endpoint before making one request.

### Libraries and tools

Use `openai` for the compatible API client and `python-dotenv` to load private
local configuration. Use Python, uv (or `venv`), Git and the AWS console.
An OpenAI account or OpenAI API key is not needed.

### Important calls and commands

`load_dotenv()` loads the local `.env` file. `OpenAI()` reads
`OPENAI_API_KEY` and `OPENAI_BASE_URL`; the variable names belong to the SDK
even though this request goes to AWS. `client.responses.create()` submits
the model and user message. `response.output_text` gives the generated text.

### Expected results

The terminal prints a one-sentence bedtime story about a unicorn. Wording
varies between runs; check that it follows the prompt rather than expecting
an exact sentence. Authentication or access failures are not successful
model responses.

### Connection to agentic AI

A model call is a building block for an agent's reasoning or response step.
Compatible APIs let you reuse client patterns across providers, while endpoint
and credential checks prevent accidental routing. This exercise generates
text only; it does not implement tools, memory or an autonomous agent loop.

## Start here

[All student labs](../../../../README.md) |
[AWS setup](../00-AWS-Lab-Setup-AWS/README.md) |
[Bedrock playground](../01-AWS-Lab-bedrock/README.md)

Complete this exercise in your separate work repository, not the public
materials clone. Use synthetic content only.

## Access and cost gate

1. Complete AWS setup and verify your trainer-approved non-root identity,
   budget notifications and available credits.
2. Confirm that your account can invoke `openai.gpt-oss-120b` through the
   Bedrock Mantle Responses API in `ap-southeast-2` (Sydney). This example
   uses a different region and model from the Nova playground lab: obtain
   trainer approval for that boundary before continuing.
3. Check current [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
   and model availability in your console. This is not a guaranteed free
   call. Budget alerts do not stop spending; make one request initially.
4. If the model, region or API-key access is unavailable, record the blocker.
   Do not enable paid billing, subscribe to another model or broaden
   permissions to bypass it.
5. Create or obtain a trainer-approved, scoped Bedrock API key through the
   [AWS API-key instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html).
   Prefer short-lived credentials. Never create root access keys or publish
   a real key in code, screenshots, chat or commits.

AWS recommends the Bedrock Runtime endpoint for new applications when the
required capabilities are supported. This exercise follows the supplied
Mantle/GPT OSS example; confirm the model's current supported route in the
[Responses API documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-responses-api.html)
before running it.

## Prepare the project

1. In your work repository, create `week1/aws/bedtime-story` and open a terminal
   there. Create an isolated environment and install the two public packages:

   ```powershell
   uv venv .venv --python 3.13
   uv pip install --python .\.venv\Scripts\python.exe openai python-dotenv
   ```

   If uv is unavailable, create the environment with
   `py -3.13 -m venv .venv` and install with
   `.\.venv\Scripts\python.exe -m pip install openai python-dotenv`.

2. Add these rules to your existing work-repository `.gitignore`, preserving
   any rules already there:

   ```gitignore
   .venv/
   .env
   .env.*
   __pycache__/
   ```

3. Create `.env` in the editor with these placeholders. Replace only the key
   placeholder privately with your own approved Bedrock key:

   ```dotenv
   OPENAI_API_KEY=<your Bedrock API key>
   OPENAI_BASE_URL=https://bedrock-mantle.ap-southeast-2.api.aws/v1
   ```

   Do not use an OpenAI key or `https://api.openai.com/v1`: those route to
   OpenAI, not AWS. The original `set NAME=...` syntax is for Command Prompt,
   not PowerShell; this lab uses `.env` to avoid putting secrets in terminal
   history. Remove conflicting inherited `OPENAI_*` variables privately if
   your terminal already has another provider configured.

4. Verify exclusion without printing the file's contents:

   ```powershell
   git check-ignore .env
   git status --short
   ```

   The first command must report `.env`; status must not list it. Stop and
   fix ignore rules if the key file is tracked or visible to Git.

## Write and run the story script

1. Create `bedtimestory.py`:

   ```python
   import os

   from dotenv import load_dotenv
   from openai import OpenAI

   load_dotenv()
   expected_url = "https://bedrock-mantle.ap-southeast-2.api.aws/v1"
   if os.environ.get("OPENAI_BASE_URL", "").rstrip("/") != expected_url:
       raise ValueError("Set OPENAI_BASE_URL to the approved Bedrock Mantle endpoint.")
   if not os.environ.get("OPENAI_API_KEY"):
       raise ValueError("Configure your private Bedrock API key before running.")

   client = OpenAI()
   response = client.responses.create(
       model="openai.gpt-oss-120b",
       input=[
           {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
       ],
   )
   print(response.output_text)
   ```

   The checks fail explicitly before a request if configuration is missing
   or points to another endpoint. They do not print credentials.

2. Run from the same work folder:

   ```powershell
   .\.venv\Scripts\python.exe bedtimestory.py
   ```

   On macOS/Linux, use `.venv/bin/python bedtimestory.py`.

3. Check that the output is one sentence, mentions a unicorn and reads like
   a bedtime story. For example, you might see:

   > A sleepy unicorn tucked the moon beneath a silver cloud and drifted into dreams.

   This is illustrative, not a recorded live response. Note whether the
   model followed the instruction; a successful API call alone does not
   prove that the content met it.

## Troubleshooting

* Missing `openai` or `dotenv`: install packages into the same `.venv`
  interpreter used to run the script.
* Endpoint configuration error: check `.env` and any inherited environment
  variables without displaying the key.
* Authentication failure: verify that you used a valid, unexpired Bedrock
  key, not an OpenAI key. Replace expired or exposed keys privately.
* Permission or model/route error: verify the approved account, Sydney region
  and current model route with the trainer; do not expand permissions.
* Rate limit or temporary service error: wait before retrying. Repeated runs
  can consume quota and credits.

## Evidence and cleanup

Commit your original `bedtimestory.py` and a short observation to your work
repository. Record the model, approved region and instruction-following result,
but no account identifiers or credential values. Confirm `.env` and `.venv`
are ignored before committing.

Revoke the lab key when no longer needed under the trainer's instructions,
and review billing. No Knowledge Base or vector store is created by this lab.
These instructions were checked for syntax and safe placeholders; no live
AWS call or account eligibility test was performed for publication.
