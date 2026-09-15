# TokenAAS Examples

Connect to production-ready AI models through one API.

[Get API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples) · [View Models](https://tokenaas.ai/model-plaza?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples) · [Documentation](https://tokenaas.ai/docs?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples) · [Service Status](https://tokenaas.ai/status?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)

## Why TokenAAS

- One OpenAI-compatible endpoint for text, image, and video models
- Anthropic-compatible `/v1/messages` for supported groups
- Change `base_url` + API key — keep your existing SDK code

```text
Base URL: https://tokenaas.ai/v1
```

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

## Trust & safety

- Text, image, and video are billed by tokens, image units, or video seconds — see [Model Plaza](https://tokenaas.ai/model-plaza)
- Check live availability on [Status](https://tokenaas.ai/status)
- Privacy: [Privacy Policy](https://tokenaas.ai/legal/privacy-policy) · Terms: [Terms of Service](https://tokenaas.ai/legal/terms)
- Security reports: `admin@tokenaas.ai`
- TokenAAS does not store your application prompts as training data for third parties through these examples; never commit API keys

## Common errors

| HTTP | Meaning | Fix |
| --- | --- | --- |
| 401 | Invalid API key | Recreate/copy the key |
| 403 | Balance / group access | Top up or bind key to an active group |
| 429 | Rate limited | Back off and retry |
| 4xx model | Model not in your group | Call `/v1/models` and use a returned ID |

## License

MIT © TokenAAS
