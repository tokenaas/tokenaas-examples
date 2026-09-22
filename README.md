# TokenAAS Examples

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Examples CI](https://github.com/tokenaas/tokenaas-examples/actions/workflows/examples-ci.yml/badge.svg)](https://github.com/tokenaas/tokenaas-examples/actions/workflows/examples-ci.yml)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-compatible-412991)](https://tokenaas.ai/docs?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](./openai-sdk/python-chat)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?logo=node.js&logoColor=white)](./openai-sdk/node-chat)

Copy-paste examples for calling production AI models through one **OpenAI-compatible** endpoint — text, image, and video. Keep your existing SDK; change `base_url` + API key.

[Get API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples) · [View Models](https://tokenaas.ai/model-plaza?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples) · [Documentation](https://tokenaas.ai/docs?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples) · [Service Status](https://tokenaas.ai/status?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples) · [Discussions](https://github.com/tokenaas/tokenaas-examples/discussions)

```text
Base URL: https://tokenaas.ai/v1
```

## Why TokenAAS

- One OpenAI-compatible endpoint for text, image, and video models
- Anthropic-compatible `/v1/messages` for supported groups
- Change `base_url` + API key — keep your existing SDK code
- DeepSeek and other production models behind the same client

## 5-minute quickstart

1. [Create an API key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
2. Export credentials:

```bash
export TOKENAAS_API_KEY="sk-..."
export TOKENAAS_BASE_URL="https://tokenaas.ai/v1"
```

3. Run a text example:

```bash
cd openai-sdk/python-chat
pip install -r requirements.txt
python main.py
```

Minimal Python shape:

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-...",
    base_url="https://tokenaas.ai/v1",
)
print(client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello"}],
).choices[0].message.content)
```

## Guides

| Guide | Level |
| --- | --- |
| [Use DeepSeek with the OpenAI Python SDK](./guides/use-deepseek-with-openai-python-sdk.md) | Beginner · 5 minutes |

Publishing drafts for DEV.to / Medium live in [`publish/`](./publish).

## Examples

| Path | What it does |
| --- | --- |
| [`openai-sdk/python-chat`](./openai-sdk/python-chat) | Python text completion |
| [`openai-sdk/python-streaming`](./openai-sdk/python-streaming) | Python streaming tokens |
| [`openai-sdk/node-chat`](./openai-sdk/node-chat) | Node.js text completion |
| [`anthropic-sdk/python-messages`](./anthropic-sdk/python-messages) | Anthropic SDK compatible call |
| [`image-generation`](./image-generation) | Image generation + save to file |
| [`video-generation`](./video-generation) | Video create → poll → download |
| [`curl`](./curl) | Raw HTTP examples |
| [`error-handling`](./error-handling) | Retries and common API errors |

Default models used in examples (override with env vars):

| Type | Model ID |
| --- | --- |
| Text | `deepseek-v4-flash` |
| Image | `Doubao-Seedream-4.5` |
| Video | `Doubao-Seedance-2.0` |

Always prefer `GET /v1/models` for the models visible to your key.

## Community

- Ask questions in [Discussions](https://github.com/tokenaas/tokenaas-examples/discussions)
- Report docs/example bugs via [Issues](https://github.com/tokenaas/tokenaas-examples/issues)
- Propose or contribute an example using the [contribution guide](./.github/CONTRIBUTING.md)
- Security reports: `admin@tokenaas.ai`

## Trust & safety

- Text, image, and video are billed by tokens, image units, or video seconds — see [Model Plaza](https://tokenaas.ai/model-plaza)
- Check live availability on [Status](https://tokenaas.ai/status)
- Privacy: [Privacy Policy](https://tokenaas.ai/legal/privacy-policy) · Terms: [Terms of Service](https://tokenaas.ai/legal/terms)
- Never commit API keys

## Common errors

| HTTP | Meaning | Fix |
| --- | --- | --- |
| 401 | Invalid API key | Recreate/copy the key |
| 403 | Balance / group access | Top up or bind key to an active group |
| 429 | Rate limited | Back off and retry |
| 4xx model | Model not in your group | Call `/v1/models` and use a returned ID |

## License

MIT © TokenAAS
