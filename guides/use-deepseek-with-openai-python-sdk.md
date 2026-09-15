# Use DeepSeek with the OpenAI Python SDK

Call `deepseek-v4-flash` through TokenAAS using the same OpenAI Python SDK you already know. You only change the base URL and API key.

**Time:** about 5 minutes  
**Runnable code:** [`openai-sdk/python-chat`](../openai-sdk/python-chat) · [`openai-sdk/python-streaming`](../openai-sdk/python-streaming)

[Get API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=guide_deepseek_openai_python) · [Model Plaza](https://tokenaas.ai/model-plaza?utm_source=github&utm_medium=repository&utm_campaign=guide_deepseek_openai_python) · [Docs](https://tokenaas.ai/docs?utm_source=github&utm_medium=repository&utm_campaign=guide_deepseek_openai_python)

---

## Why this works

TokenAAS exposes an OpenAI-compatible Chat Completions API at:

```text
https://tokenaas.ai/v1
```

DeepSeek models available through your key (for example `deepseek-v4-flash`) accept the same `chat.completions.create` shape as OpenAI. Existing apps usually need:

1. A TokenAAS API key
2. `base_url="https://tokenaas.ai/v1"`
3. A model ID returned by `GET /v1/models`

No proprietary client library is required.

---

## Prerequisites

- Python 3.9+
- A TokenAAS account with balance or quota
- An API key bound to a group that includes DeepSeek text models

Create a key here: [tokenaas.ai/register](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=guide_deepseek_openai_python)

---

## 1. Install the OpenAI SDK

```bash
pip install "openai>=1.40.0"
```

---

## 2. Set environment variables

```bash
export TOKENAAS_API_KEY="sk-..."
export TOKENAAS_BASE_URL="https://tokenaas.ai/v1"
export TOKENAAS_TEXT_MODEL="deepseek-v4-flash"
```

Never commit the key to git or put it in frontend code.

Optional: confirm the model is visible to your key:

```bash
curl "$TOKENAAS_BASE_URL/models" \
  -H "Authorization: Bearer $TOKENAAS_API_KEY"
```

Use an exact `id` from that response if your group uses a different DeepSeek variant (for example `deepseek-v4-pro`).

---

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

Run the checked-in copy:

```bash
cd openai-sdk/python-chat
pip install -r requirements.txt
python main.py
```

**Expected result:** a short assistant reply printed to the terminal.

---

## 4. Streaming tokens

For chat UIs and CLIs, enable streaming:

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

Runnable path: [`openai-sdk/python-streaming`](../openai-sdk/python-streaming)

```bash
cd openai-sdk/python-streaming
pip install -r requirements.txt
python main.py
```

---

## 5. What to change if you already use OpenAI

| Setting | OpenAI default | TokenAAS |
| --- | --- | --- |
| SDK package | `openai` | same |
| `api_key` | OpenAI key | TokenAAS key |
| `base_url` | (SDK default) | `https://tokenaas.ai/v1` |
| `model` | e.g. `gpt-4o-mini` | e.g. `deepseek-v4-flash` |

Everything else in a typical chat completion call stays the same: `messages`, `stream`, `temperature`, tool calling (when the model/group supports it), and response parsing.

---

## 6. Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `401` | Bad or missing key | Recreate the key; export `TOKENAAS_API_KEY` again |
| `403` insufficient balance | Empty wallet / quota | Top up or check subscription |
| `403` group errors | Key not bound to an active group | Bind the key in the console |
| `429` | Rate limit | Back off; reduce concurrency |
| Model not found | ID not in this key’s group | Call `/v1/models` and use a returned ID |

When contacting support, send the HTTP status, error `code` / `message`, and request ID — never the full API key.

More patterns: [`error-handling`](../error-handling)

---

## 7. Next steps

- Try image or video examples: [`image-generation`](../image-generation), [`video-generation`](../video-generation)
- Browse live models and pricing: [Model Plaza](https://tokenaas.ai/model-plaza?utm_source=github&utm_medium=repository&utm_campaign=guide_deepseek_openai_python)
- Full API docs: [tokenaas.ai/docs](https://tokenaas.ai/docs?utm_source=github&utm_medium=repository&utm_campaign=guide_deepseek_openai_python)

---

## Publish note

This guide is meant to be reused on DEV, Hashnode, or Medium. Keep the runnable links pointing at:

https://github.com/tokenaas/tokenaas-examples
