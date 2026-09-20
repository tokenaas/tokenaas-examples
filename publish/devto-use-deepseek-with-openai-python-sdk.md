---
title: Use DeepSeek with the OpenAI Python SDK in 5 Minutes
published: false
description: Call DeepSeek through an OpenAI-compatible base_url without rewriting your app. Includes non-streaming and streaming examples.
tags: python, openai, deepseek, llm, ai
canonical_url:
---

# Use DeepSeek with the OpenAI Python SDK in 5 Minutes

If your app already uses the official OpenAI Python SDK, you do not need a new client library to try DeepSeek. Point the same SDK at an OpenAI-compatible endpoint, swap the API key and model ID, and keep `chat.completions.create` as-is.

This walkthrough uses [TokenAAS](https://tokenaas.ai/register?utm_source=devto&utm_medium=article&utm_campaign=guide_deepseek_openai_python) as that endpoint. Runnable copies live in the open-source repo:

**https://github.com/tokenaas/tokenaas-examples**

- Guide in the repo: [Use DeepSeek with the OpenAI Python SDK](https://github.com/tokenaas/tokenaas-examples/blob/main/guides/use-deepseek-with-openai-python-sdk.md)
- Code: [`openai-sdk/python-chat`](https://github.com/tokenaas/tokenaas-examples/tree/main/openai-sdk/python-chat) · [`openai-sdk/python-streaming`](https://github.com/tokenaas/tokenaas-examples/tree/main/openai-sdk/python-streaming)

**Time:** about 5 minutes  
**Requires:** Python 3.9+, an API key with access to a DeepSeek text model

---

## Why this works

TokenAAS exposes Chat Completions at:

```text
https://tokenaas.ai/v1
```

DeepSeek models available through your key (for example `deepseek-v4-flash`) accept the same request shape as OpenAI. Existing apps usually need only:

1. A TokenAAS API key
2. `base_url="https://tokenaas.ai/v1"`
3. A model ID returned by `GET /v1/models`

No proprietary SDK required.

---

## 1. Install the OpenAI SDK

```bash
pip install "openai>=1.40.0"
```

## 2. Set environment variables

```bash
export TOKENAAS_API_KEY="sk-..."
export TOKENAAS_BASE_URL="https://tokenaas.ai/v1"
export TOKENAAS_TEXT_MODEL="deepseek-v4-flash"
```

Never commit the key or put it in frontend code.

Optional — confirm the model is visible to your key:

```bash
curl "$TOKENAAS_BASE_URL/models" \
  -H "Authorization: Bearer $TOKENAAS_API_KEY"
```

Use an exact `id` from that response if your group uses a different DeepSeek variant (for example `deepseek-v4-pro`).

Create a key here if you do not have one yet: [tokenaas.ai/register](https://tokenaas.ai/register?utm_source=devto&utm_medium=article&utm_campaign=guide_deepseek_openai_python)

## 3. Non-streaming request

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["TOKENAAS_API_KEY"],
    base_url=os.environ.get("TOKENAAS_BASE_URL", "https://tokenaas.ai/v1"),
    timeout=60.0,
    max_retries=2,
)

response = client.chat.completions.create(
    model=os.environ.get("TOKENAAS_TEXT_MODEL", "deepseek-v4-flash"),
    messages=[
        {
            "role": "user",
            "content": "Explain large language models in three sentences.",
        }
    ],
)

print(response.choices[0].message.content)
```

Or clone and run the checked-in example:

```bash
git clone https://github.com/tokenaas/tokenaas-examples.git
cd tokenaas-examples/openai-sdk/python-chat
pip install -r requirements.txt
python main.py
```

**Expected result:** a short assistant reply in the terminal.

## 4. Streaming tokens

```python
stream = client.chat.completions.create(
    model=os.environ.get("TOKENAAS_TEXT_MODEL", "deepseek-v4-flash"),
    messages=[{"role": "user", "content": "Write a short story about a lighthouse."}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
```

Runnable path: [`openai-sdk/python-streaming`](https://github.com/tokenaas/tokenaas-examples/tree/main/openai-sdk/python-streaming)

## 5. What to change if you already use OpenAI

| Setting | OpenAI default | TokenAAS |
| --- | --- | --- |
| SDK package | `openai` | same |
| `api_key` | OpenAI key | TokenAAS key |
| `base_url` | (SDK default) | `https://tokenaas.ai/v1` |
| `model` | e.g. `gpt-4o-mini` | e.g. `deepseek-v4-flash` |

`messages`, `stream`, `temperature`, and normal response parsing stay the same. Tool calling works when the model/group supports it.

## 6. Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `401` | Bad or missing key | Recreate the key; export `TOKENAAS_API_KEY` again |
| `403` insufficient balance | Empty wallet / quota | Top up or check subscription |
| `403` group errors | Key not bound to an active group | Bind the key in the console |
| `429` | Rate limit | Back off; reduce concurrency |
| Model not found | ID not in this key’s group | Call `/v1/models` and use a returned ID |

When contacting support, send the HTTP status, error `code` / `message`, and request ID — never the full API key.

More patterns: [error-handling example](https://github.com/tokenaas/tokenaas-examples/tree/main/error-handling)

## Next steps

- Image / video examples: [image-generation](https://github.com/tokenaas/tokenaas-examples/tree/main/image-generation) · [video-generation](https://github.com/tokenaas/tokenaas-examples/tree/main/video-generation)
- Live models and pricing: [Model Plaza](https://tokenaas.ai/model-plaza?utm_source=devto&utm_medium=article&utm_campaign=guide_deepseek_openai_python)
- API docs: [tokenaas.ai/docs](https://tokenaas.ai/docs?utm_source=devto&utm_medium=article&utm_campaign=guide_deepseek_openai_python)
- Questions: [GitHub Discussions](https://github.com/tokenaas/tokenaas-examples/discussions)

---

### Publish checklist (for you)

1. Copy this file into DEV.to → New post (or Medium / Hashnode).
2. Set tags: `python`, `openai`, `deepseek`, `llm` (adjust to platform limits).
3. Keep UTM links as-is so you can measure signups from this article.
4. After publish, paste the public URL into a GitHub Discussion comment and pin/link it from the repo README Guides table if useful.
