# Error handling

Demonstrate bounded retries and readable handling of common TokenAAS API errors.

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

## What it covers

- Missing / invalid credentials messaging
- Retry on `429` and transient `5xx`
- Logging status and request id without printing the API key

## Get started

[Create API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
