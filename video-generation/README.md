# Video generation

Create an async video task, poll until success, then download the MP4.

Default model: `Doubao-Seedance-2.0` (override with `TOKENAAS_VIDEO_MODEL`).

**Billing note:** video generation charges real balance by duration/resolution. Start with short clips and low resolution.

## Requirements

- Python 3.9+
- API key with a video-capable model
- Sufficient balance

## Install

```bash
pip install -r requirements.txt
```

## Environment

```bash
export TOKENAAS_API_KEY="sk-..."
export TOKENAAS_BASE_URL="https://tokenaas.ai/v1"
export TOKENAAS_VIDEO_MODEL="Doubao-Seedance-2.0"
```

## Run

```bash
python main.py
```

## Expected response

Polls until `succeeded`, then writes `output/result.mp4`.

## Common errors

- `400` — unsupported duration/resolution combination
- `402` — insufficient balance for the reserved charge
- Long `processing` — wait; do not recreate tasks in a tight loop

## Get started

[Create API Key](https://tokenaas.ai/register?utm_source=github&utm_medium=repository&utm_campaign=tokenaas_examples)
