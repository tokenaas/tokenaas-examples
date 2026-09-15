# Anthropic SDK (compatible messages API)

Call TokenAAS with the Anthropic Python SDK when your key's group exposes an Anthropic-protocol model.

> Tip: list models with `GET /v1/models` and pick an ID your group supports. If your group only has OpenAI-compatible models, use the OpenAI SDK examples instead.

## Requirements

- Python 3.9+
- API key bound to a group that supports Anthropic-protocol models

## Install

```bash
pip install -r requirements.txt
```

## Environment

```bash
export TOKENAAS_API_KEY="sk-..."
# Anthropic SDK expects the host root; TokenAAS serves messages at /v1/messages
export TOKENAAS_ANTHROPIC_BASE_URL="https://tokenaas.ai"
export TOKENAAS_ANTHROPIC_MODEL="YOUR_ANTHROPIC_MODEL"
```

## Run

```bash
python main.py
```

## Expected response

Prints the first text block from the Anthropic message response.

## Common errors

- Model unavailable — confirm the group supports Anthropic protocol
- `401` — use `x-api-key` style auth via the SDK (`api_key=...`)

## Get started

[Create API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
