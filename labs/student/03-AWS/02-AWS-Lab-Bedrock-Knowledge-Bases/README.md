---
title: "02-AWS-Lab-Bedrock-Knowledge-Bases"
description: Observe an instructor demo of managed RAG over public UAE policy documents.
id: A02
cloud: AWS
difficulty: Foundation
lab_type: Instructor demo
release_date: 2026-10-31
estimated_minutes: 30
course_slide: 142
dependencies: [CH00, A00, A01, P01, G02]
---

## Start here

[All student labs](../../../../README.md) |
[AWS setup](../00-AWS-Lab-Setup-AWS/README.md) |
[AWS Bedrock playground](../01-AWS-Lab-bedrock/README.md) |
[Python RAG](../../01-Python/01-Python-Lab-RAG/README.md) |
[Gemini File Search](../../02-Google-AI-Studio/02-GAIS-Lab-Embedding-File-Search/README.md)

## Lab overview

| Field | Details |
| --- | --- |
| Course exercise | AWS Lab 2: Amazon Bedrock Knowledge Bases |
| Type | Instructor demo; students observe and record comparisons |
| Duration | 25 to 30 minutes |
| Course slide | 142 |
| Environment | Instructor's authorized AWS account, console and optional CloudShell |
| Student deliverable | Comparison table in a separate work/submission repository |

> [!WARNING]
> Students must not provision resources just to follow this demonstration.
> The instructor must verify service availability, permissions and current
> pricing before starting. Free-plan eligibility does not guarantee access to
> Knowledge Bases, embedding models or vector stores. Do not upgrade billing
> or broaden permissions to bypass a restriction. Budget alerts do not cap costs.

The instructor builds a knowledge base over the same UAE policy documents,
tests retrieval and generation with citations, and deletes the resources in
front of the class. Students compare it with local Python RAG and Gemini File
Search. If an authorized live demonstration is unavailable, record that
limitation rather than presenting an offline walkthrough as a live test.

## Before you start

1. Review AWS setup: MFA, non-root temporary service identity, billing alerts,
   remaining credits and the authorized region, normally `us-east-1`.
2. Obtain the three public documents using the Python RAG instructions:
   `uae_ai_charter.txt`, `uae_ai_ethics_guidelines.pdf` and
   `dubai_ai_ethics_guidelines.pdf`. Keep attribution.
3. Have the Python RAG `eval.csv` and Gemini comparison results ready.
4. Use only public or synthetic data. Never publish account IDs, keys, credentials
   or unredacted console screenshots.
5. The instructor checks the official
   [Knowledge Bases documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
   and [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

## Instructor: upload the documents to S3

1. Open S3 and select Create bucket.
2. Choose a globally unique example name such as `kb-demo-yourname-2026` and
   the authorized region. Keep Block all public access enabled.
3. Open the bucket, select Upload, add the three documents and upload them.
4. Record the task-owned bucket privately for cleanup; do not include account
   identifiers in student evidence.

## Instructor: create the knowledge base

1. Open Amazon Bedrock, select Knowledge bases, then Create and Knowledge base
   with vector store.
2. Name it `uae-policies-kb`. Use a new task-scoped service role only if the
   instructor is authorized to create it; review its permissions.
3. Choose Amazon S3 as the data source and select the demo bucket. Keep default
   parsing and chunking for the first run.
4. Select an authorized embedding model, such as Titan Text Embeddings V2.
   If comparing an approved multilingual Cohere model, review access and pricing
   first. Multilingual retrieval matters for Arabic questions.
5. Select Quick create a new vector store and Amazon S3 Vectors when available
   in the approved account and region. If unavailable, stop rather than silently
   substituting a different billable service.
6. Review the resources and create the knowledge base. Creation may take a few
   minutes. Record the vector bucket/index and service role for later cleanup.

> [!CAUTION]
> Do not leave an OpenSearch Serverless collection running. Minimum capacity
> charges can accrue while it exists, even without queries. Deleting a knowledge
> base does not necessarily delete its vector store.

## Instructor: sync and test citations

1. Select the data source and Sync. Bedrock reads, chunks and embeds the
   documents, then writes vectors to the store. Sync again after document changes.
2. In Test knowledge base, select an authorized generation model and ask:

   ```text
   Which principle in the UAE AI Charter covers human oversight?
   ```

3. Open source details. Inspect the retrieved passages and their S3 locations.
4. Turn generation off and repeat the question to inspect retrieval-only chunks
   and scores separately from the answer.
5. Ask an Arabic question from `eval.csv`, then an unanswerable question:

   ```text
   What is the fine for breaking the UAE AI Charter?
   ```

6. Record whether the answer declines when the documents do not contain it.
   Do not infer correctness from the presence of citations alone.

## Optional instructor code in CloudShell

Use a trainer-approved non-root temporary session in the authorized region.
Create `kb_query.py`, replace the placeholders privately with the demo's
knowledge base ID and approved generation model ARN, and run `python kb_query.py`.
Do not commit those identifiers or the raw response.

```python
"""Ask the knowledge base from code. Run in AWS CloudShell in us-east-1."""
import boto3

KB_ID = "<knowledge base ID>"
MODEL_ARN = "<model ARN>"

client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")
response = client.retrieve_and_generate(
    input={"text": "Which principle in the UAE AI Charter covers human oversight?"},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": KB_ID,
            "modelArn": MODEL_ARN,
        },
    },
)
print(response["output"]["text"])
for citation in response.get("citations", []):
    for reference in citation.get("retrievedReferences", []):
        print("-", reference["location"]["s3Location"]["uri"])
```

## Students: record the differences

Use the same five evaluation questions for each approach, including Arabic and
an unanswerable question. Record observed results, not assumed outcomes.

| Criterion | Python RAG | Gemini File Search | Bedrock Knowledge Bases |
| --- | --- | --- | --- |
| Setup time | | | |
| Code written | | | |
| Correct answers out of five | | | |
| Citation quality | | | |
| Arabic question handled | | | |
| Unanswerable question declined | | | |
| Data storage location | | | |
| Cleanup steps | | | |
| Live demonstration or unavailable | | | |

Commit your comparison table to your separate work repository. Explain the
trade-off: managed RAG removes some chunking, embedding and indexing code, but
reduces direct control and introduces service/storage costs.

## Instructor: cleanup in front of the class

1. Delete `uae-policies-kb` from Bedrock Knowledge bases.
2. Delete the task-owned vector store separately: the S3 vector index and vector
   bucket, or any explicitly approved OpenSearch collection used for the demo.
3. Empty and delete the task-owned document S3 bucket. Check versioned objects
   if versioning was enabled.
4. Delete the newly created task-only IAM role if no other resources depend on
   it. Never delete shared institutional roles or buckets.
5. Open Billing and Cost Management and inspect Bills and Credits. Check again
   the next day because usage and charges may appear later.
6. Verify that the demo resources are gone; trial expiry is not cleanup.

## Troubleshooting and validation limits

* Service or vector-store option unavailable: stop and record the account/region
  restriction without upgrading or substituting paid infrastructure.
* Sync fails: inspect the authorized role, data source and model permissions;
  sanitize error evidence before sharing.
* Weak Arabic retrieval: compare the approved embedding model and retrieved
  passages before judging generation.
* Resources remain after deleting the knowledge base: inspect the separate
  vector store and S3 bucket cleanup.

The source course guide describes the signed-in console flow rather than
showing it. Its optional request was validated offline against the boto3 1.43
service model. This publication does not claim a new live AWS test.
