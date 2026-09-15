# Python streaming (OpenAI SDK)

Stream assistant tokens as they arrive.

## Requirements

- Python 3.9+
- TokenAAS API key

## Install

```bash
pip install -r requirements.txt
```

## Environment

```bash
export TOKENAAS_API_KEY="sk-..."
export TOKENAAS_BASE_URL="https://tokenaas.ai/v1"
export TOKENAAS_TEXT_MODEL="deepseek-v4-flash"
```

## Run

```bash
python main.py
```

## Expected response

Tokens print continuously to the terminal without waiting for the full reply.

## Common errors

Same as [`../python-chat`](../python-chat). Use `curl -N` style streaming mentally: keep the connection open until done.

## Get started

[Create API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
