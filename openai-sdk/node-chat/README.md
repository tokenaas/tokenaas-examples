# Node.js chat (OpenAI SDK)

Text completion using the official OpenAI Node SDK pointed at TokenAAS.

## Requirements

- Node.js 18+
- TokenAAS API key

## Install

```bash
npm install
```

## Environment

```bash
export TOKENAAS_API_KEY="sk-..."
export TOKENAAS_BASE_URL="https://tokenaas.ai/v1"
export TOKENAAS_TEXT_MODEL="deepseek-v4-flash"
```

## Run

```bash
node main.mjs
```

## Expected response

Prints the assistant message content.

## Common errors

- Missing env → script exits with a clear error
- `401` / `403` / `429` → see root README troubleshooting table

## Get started

[Create API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
