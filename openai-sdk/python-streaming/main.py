"""Streaming chat completion via the OpenAI Python SDK."""

from __future__ import annotations

import os
import sys

from openai import OpenAI


def main() -> None:
    api_key = os.environ.get("TOKENAAS_API_KEY")
    if not api_key:
        print("Set TOKENAAS_API_KEY first.", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(
        api_key=api_key,
        base_url=os.environ.get("TOKENAAS_BASE_URL", "https://tokenaas.ai/v1"),
        timeout=60.0,
        max_retries=2,
    )

    model = os.environ.get("TOKENAAS_TEXT_MODEL", "deepseek-v4-flash")
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Write a short story about a lighthouse."}],
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
