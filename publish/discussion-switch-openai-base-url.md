# Discussion draft — post as category: General (or Q&A)

**Suggested title:** How to point an existing OpenAI SDK app at a custom `base_url` (DeepSeek example)

**Body (copy below the line):**

---

If you already ship with the official OpenAI Python or Node SDK, switching providers often means **two lines**, not a rewrite:

1. Set `base_url` to an OpenAI-compatible gateway
2. Swap the API key and model ID

For TokenAAS that looks like:

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-...",                 # TokenAAS key
    base_url="https://tokenaas.ai/v1",
)

resp = client.chat.completions.create(
    model="deepseek-v4-flash",        # or any id from GET /v1/models
    messages=[{"role": "user", "content": "ping"}],
)
print(resp.choices[0].message.content)
```

Node is the same idea (`baseURL` / `apiKey` depending on SDK version).

### Checklist before you cut over

- [ ] Call `GET /v1/models` with your key and copy an exact model `id`
- [ ] Keep retries/timeouts — gateways still rate-limit (`429`)
- [ ] Do not hardcode keys in frontend bundles
- [ ] Confirm the key’s group includes the model you want (text vs image vs video)

### Runnable examples

- Python chat: https://github.com/tokenaas/tokenaas-examples/tree/main/openai-sdk/python-chat
- Streaming: https://github.com/tokenaas/tokenaas-examples/tree/main/openai-sdk/python-streaming
- Full guide: https://github.com/tokenaas/tokenaas-examples/blob/main/guides/use-deepseek-with-openai-python-sdk.md

### Questions for the thread

- Are you migrating from OpenAI direct, Azure OpenAI, or another compatible proxy?
- Text only, or do you also need image / video on the same key?

Drop errors (status + message, **no API key**) below and we can help debug.

Docs: https://tokenaas.ai/docs?utm_source=github&utm_medium=discussion&utm_campaign=base_url_switch  
Register: https://tokenaas.ai/register?utm_source=github&utm_medium=discussion&utm_campaign=base_url_switch
