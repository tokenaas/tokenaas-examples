# Image generation

Generate an image with TokenAAS and save it locally.

Default model: `Doubao-Seedream-4.5` (override with `TOKENAAS_IMAGE_MODEL`).

Some Seedream models require large pixel counts; `2048x2048` is a safe starting size.

## Requirements

- Python 3.9+
- API key with an image-capable model
- Balance sufficient for image billing

## Install

```bash
pip install -r requirements.txt
```

## Environment

```bash
export TOKENAAS_API_KEY="sk-..."
export TOKENAAS_BASE_URL="https://tokenaas.ai/v1"
export TOKENAAS_IMAGE_MODEL="Doubao-Seedream-4.5"
```

## Run

```bash
python main.py
```

## Expected response

Writes `output/generated.png` (or downloads from a returned URL).

## Common errors

- `400 InvalidParameter` — unsupported size for the model
- `402` / insufficient balance — top up before retrying
- `404` — model/endpoint not available for this key

## Get started

[Create API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
