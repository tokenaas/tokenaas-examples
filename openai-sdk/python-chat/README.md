# Python chat (OpenAI SDK)

Non-streaming text request against TokenAAS.

## Requirements

- Python 3.9+
- TokenAAS API key with a text model in the bound group

## Install

```bash
pip install -r requirements.txt
```

## Environment

```bash
export TOKENAAS_API_KEY="sk-..."
export TOKENAAS_BASE_URL="https://tokenaas.ai/v1"   # optional
export TOKENAAS_TEXT_MODEL="deepseek-v4-flash"      # optional
```

## Run

```bash
python main.py
```

## Expected response

Prints the assistant message text, for example:

```text
Hello! How can I help you today?
```

## Common errors

- `401` — check `TOKENAAS_API_KEY`
- `403` — insufficient balance or group disabled
- Model not found — run `curl "$TOKENAAS_BASE_URL/models" -H "Authorization: Bearer $TOKENAAS_API_KEY"`

## Get started

[Create API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
